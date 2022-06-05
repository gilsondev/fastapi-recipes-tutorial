from app.schemas import Recipe
from app.schemas import RecipeCreate
from app.schemas import RecipeSearchResults


def test_recipe_schema(recipe_raw):
    recipe = Recipe(**recipe_raw)
    fields = list(recipe.__dict__.keys())

    assert ["label", "source", "url", "id"] == fields
    assert recipe.id == recipe_raw["id"]
    assert recipe.label == recipe_raw["label"]
    assert recipe.source == recipe_raw["source"]
    assert recipe.url == recipe_raw["url"]


def test_recipesearchresults_schema(recipe_raw):
    recipe = Recipe(**recipe_raw)
    data = {"results": [recipe]}
    results = RecipeSearchResults(**data)
    fields = list(results.__dict__.keys())

    assert ["results"] == fields


def test_recipe_create_schema(recipe_raw):
    recipe_raw["submitter_id"] = 10
    recipe = RecipeCreate(**recipe_raw)
    fields = list(recipe.__dict__.keys())

    assert ["label", "source", "url", "id", "submitter_id"] == fields
    assert recipe.id == recipe_raw["id"]
    assert recipe.label == recipe_raw["label"]
    assert recipe.source == recipe_raw["source"]
    assert recipe.url == recipe_raw["url"]
