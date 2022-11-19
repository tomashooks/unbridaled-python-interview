import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings


@lru_cache()
def load_env() -> bool:
    return load_dotenv()


load_env()


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    database_url: str = os.environ["DATABASE_URL"]
    # we need to test on the same DB type to avoid mistakes
    database_test_url: str = os.environ["DATABASE_TEST_URL"]
    fastapi_kwargs: dict = {}


@lru_cache()
def get_settings() -> Settings:
    return Settings()
