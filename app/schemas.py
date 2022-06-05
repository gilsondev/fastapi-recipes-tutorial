from typing import Sequence

from pydantic import BaseModel
from pydantic.networks import HttpUrl


class RecipeBase(BaseModel):
    label: str
    source: str
    url: HttpUrl


class Recipe(RecipeBase):
    id: int


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]


class RecipeCreate(RecipeBase):
    id: int
    submitter_id: int
