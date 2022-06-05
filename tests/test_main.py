import app


def test_root_endpoint(client):
    resp = client.get("/")

    assert resp.status_code == 200
    assert resp.json() == {"msg": app.__project__, "version": app.__version__}


def test_fetch_recipe_endpoint(client, recipes, mocker):
    mocker.patch("app.main.RECIPES", recipes)
    resp = client.get("/recipe/1")

    assert resp.status_code == 200


def test_fetch_recipe_not_found(client, recipes, mocker):
    mocker.patch("app.main.RECIPES", recipes)
    resp = client.get("/recipe/999")

    assert resp.status_code == 404


def test_search_recipes_endpoint(client, recipes, mocker):
    mocker.patch("app.main.RECIPES", recipes)
    resp = client.get("/search/?keyword=Tofu")

    assert resp.status_code == 200
    results = resp.json()["results"]

    assert len(results) == 1


def test_search_recipes_endpoint_without_keyword(client, recipes, mocker):
    mocker.patch("app.main.RECIPES", recipes)
    resp = client.get("/search/")

    assert resp.status_code == 200
    results = resp.json()["results"]

    assert len(results) == 3


def test_create_recipe(client, recipes, recipe_raw, mocker):
    data = {**recipe_raw, "submitter_id": 10}
    mocker.patch("app.main.RECIPES", recipes)
    resp = client.post("/recipe/", json=data)

    assert resp.status_code == 201
