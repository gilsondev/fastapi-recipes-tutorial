from typing import Any
from typing import Optional

from fastapi import APIRouter
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Query
from fastapi import Request
from fastapi import templating

from app import __project__
from app import __version__
from app import config
from app.schemas import Recipe
from app.schemas import RecipeCreate
from app.schemas import RecipeSearchResults

RECIPES = [
    {
        "id": 1,
        "label": "Chicken Vesuvio",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html",
    },
    {
        "id": 2,
        "label": "Chicken Paprikash",
        "source": "No Recipes",
        "url": "http://norecipes.com/recipe/chicken-paprikash/",
    },
    {
        "id": 3,
        "label": "Cauliflower and Tofu Curry Recipe",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/02/cauliflower-and-tofu-curry-recipe.html",
    },
]


app = FastAPI(title=__project__, openapi_url="/openapi.json")
templates = templating.Jinja2Templates(directory=str(config.TEMPLATES))
router = APIRouter()


@router.get("/about", status_code=200)
def about() -> dict:
    """Room GET"""
    return {"msg": "Recipes API", "version": __version__}


@router.get("/", status_code=200)
def root(request: Request) -> Any:
    """Homepage"""
    return templates.TemplateResponse(
        "index.html", {"request": request, "recipes": RECIPES}
    )


@router.get("/recipe/{recipe_id}", status_code=200, response_model=Recipe)
def fetch_recipe(*, recipe_id: int) -> dict:
    """Fetch a single recipe by ID"""
    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]

    if not result:
        raise HTTPException(status_code=404, detail="Recipe not found")

    return result[0]


@router.get("/search/", status_code=200, response_model=RecipeSearchResults)
def search_recipes(
    keyword: Optional[str] = Query("", min_length=3, example="chicken"),
    max_results: Optional[int] = 10,
) -> dict:
    """Search for recipes based on label keyword"""
    search_recipes = (
        lambda recipe: keyword.lower() in recipe["label"].lower()  # type: ignore
    )  # noqa
    results = filter(search_recipes, RECIPES)

    return {"results": list(results)[:max_results]}


@router.post("/recipe/", status_code=201, response_model=Recipe)
def create_recipe(*, recipe_in: RecipeCreate) -> dict:
    new_entry_id = len(RECIPES) + 1
    recipe_entry = Recipe(
        id=new_entry_id,
        label=recipe_in.label,
        source=recipe_in.source,
        url=recipe_in.url,
    )
    RECIPES.append(recipe_entry.dict())
    return recipe_entry.dict()


app.include_router(router)

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")  # type: ignore
