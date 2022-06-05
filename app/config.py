from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent
SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"

TEMPLATES = BASE_PATH / "templates"
