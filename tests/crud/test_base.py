from app.crud.base import CRUDBase
from app.models import Recipe
from app.schemas import RecipeCreate
from app.schemas import RecipeUpdate

recipeCrud = CRUDBase(Recipe)


def test_fetch_crud_base(db_session, recipe_model):
    result = recipeCrud.get(db=db_session, id=recipe_model.id)

    assert result
    assert result.id == recipe_model.id
    assert result.label == recipe_model.label


def test_fetch_multi_crud_base(db_session, recipe_model):
    result = recipeCrud.get_multi(db=db_session, skip=0, limit=100)

    assert result
    assert len(result) > 0
    assert result[0].id == recipe_model.id


def test_create_crud_base(db_session, recipe_raw):
    recipe = RecipeCreate(**recipe_raw)
    created_recipe = recipeCrud.create(db=db_session, obj_in=recipe)

    assert created_recipe
    assert created_recipe in db_session
    assert created_recipe.id


def test_update_crud_base(db_session, recipe_schema, recipe_model):
    update_data = RecipeUpdate(
        source=recipe_schema.source, url=recipe_schema.url, label="updated_recipe"
    )
    result = recipeCrud.update(db=db_session, db_obj=recipe_model, obj_in=update_data)

    assert result
    assert result.id
    assert result.label == update_data.label


def test_delete_crud_base(db_session, recipe_model):
    assert recipe_model in db_session

    result = recipeCrud.remove(db=db_session, id=recipe_model.id)

    assert result not in db_session
    assert recipe_model not in db_session
