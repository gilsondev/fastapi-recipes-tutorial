import pytest
from fastapi.testclient import TestClient
from sqlalchemy.engine.base import Connection
from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker

from app import main
from app import models


@pytest.fixture(scope="session")
def db_connection():
    engine = create_engine("sqlite://")  # in-memory database
    return engine.connect()


@pytest.fixture(scope="session")
def setup_database(db_connection: Connection):
    models.Base.metadata.bind = db_connection  # type: ignore
    models.Base.metadata.create_all()  # type: ignore

    yield

    models.Base.metadata.drop_all()  # type: ignore


@pytest.fixture(scope="session")
def client():
    return TestClient(main.app)


@pytest.fixture
def db_session(setup_database, db_connection: Connection):
    transaction = db_connection.begin()

    yield scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=db_connection)
    )
    transaction.rollback()


@pytest.fixture
def recipe_raw():
    return {
        "id": 1,
        "label": "Chicken Vesuvio",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html",
        "submitter_id": 10,
    }


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


@pytest.fixture
def recipe_model(recipe_raw, db_session):
    recipe = models.Recipe(**recipe_raw)
    db_session.add(recipe)
    db_session.commit()
    db_session.refresh(recipe)

    return recipe
