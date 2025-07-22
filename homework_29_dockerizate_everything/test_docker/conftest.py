import pytest

from homework_22_alchemi.data_provider.course import get_course
from homework_22_alchemi.university import Courses, Students
from homework_22_alchemi.alchemi_client import SQLAlchemyClient
import os


@pytest.fixture(scope="session")
def db_client():
    client = SQLAlchemyClient(os.getenv("db_url"))
    client.create_table(Courses)
    client.create_table(Students)
    for _ in range(5):
        new_course = get_course()
        if not client.session.query(Courses).filter_by(name=new_course["name"]).first():
            client.session.add(Courses(**new_course))
    client.session.commit()
    client.add_student()
    yield client
    client.close_connection()
