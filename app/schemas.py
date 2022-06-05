from typing import Sequence
from pydantic import BaseModel
from pydantic.networks import HttpUrl


class Recipe(BaseModel):
    id: int
    label: str
    source: str
    url: HttpUrl


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]


class RecipeCreate(BaseModel):
    id: int
    label: str
    source: str
    url: HttpUrl
    submitter_id: int
