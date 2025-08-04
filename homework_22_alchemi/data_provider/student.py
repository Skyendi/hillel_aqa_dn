from faker import Faker
import random
import allure

fake = Faker()

@allure.step("get_student")
def get_student(existing_course_ids):
    student = {"name": fake.name(),
               "course_id": random.choice(existing_course_ids)
               }
    return student


