from typing import Sequence

from pydantic import BaseModel
from pydantic.networks import HttpUrl


class RecipeBase(BaseModel):
    label: str
    source: str
    url: HttpUrl


class RecipeCreate(RecipeBase):
    id: int
    submitter_id: int


class RecipeUpdate(RecipeBase):
    label: str


class RecipeInDBBase(RecipeBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True


class Recipe(RecipeInDBBase):
    pass


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]


class RecipeInDB(RecipeInDBBase):
    pass
