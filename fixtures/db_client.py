import pytest
from utils.database import PostresDB


@pytest.fixture(scope='session')
def db_client():
    db = PostresDB()
    yield db
    db.close()