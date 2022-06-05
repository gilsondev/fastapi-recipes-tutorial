from typing import Optional

from fastapi import FastAPI, APIRouter, HTTPException

from app import __version__, __project__

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
router = APIRouter()


@router.get("/", status_code=200)
def root() -> dict:
    """Room GET"""
    return {"msg": "Recipes API", "version": __version__}


@router.get("/recipe/{recipe_id}", status_code=200)
def fetch_recipe(*, recipe_id: int) -> dict:
    """Fetch a single recipe by ID"""
    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]

    if not result:
        raise HTTPException(status_code=404, detail="Recipe not found")

    return result[0]


@router.get("/search/", status_code=200)
def search_recipes(
    keyword: Optional[str] = "", max_results: Optional[int] = 10
) -> dict:
    """Search for recipes based on label keyword"""
    search_recipes = (
        lambda recipe: keyword.lower() in recipe["label"].lower()  # type: ignore
    )  # noqa
    results = filter(search_recipes, RECIPES)

    return {"results": list(results)[:max_results]}


app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
