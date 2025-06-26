from faker import Faker
from random import randint

from fixtures import db_client
from homework_22_alchemi.university import Courses

fake = Faker()


def get_student():

    student = {"name": fake.name(),
               "course_id": randint(8,12)
               }
    return student

# print(get_student())
