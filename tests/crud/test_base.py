from app.crud.base import CRUDBase
from app.models import Recipe

recipeCrud = CRUDBase(Recipe)


def test_fetch_crud_base(db_session, recipe_model):
    result = recipeCrud.get(db=db_session, id=recipe_model.id)

    assert result
    assert result.id == recipe_model.id
    assert result.label == recipe_model.label
