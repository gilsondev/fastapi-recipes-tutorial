import pytest

from fastapi.testclient import TestClient

from app import main


@pytest.fixture(scope="session")
def client():
    return TestClient(main.app)


@pytest.fixture
def recipes():
    return [
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
