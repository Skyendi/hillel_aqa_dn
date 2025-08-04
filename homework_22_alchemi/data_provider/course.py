from random import choice, random
import random
import allure


def random_course():

    courses = [{"name": "Software Engineering"},
               {"name":"Computer Networks and the Internet"},
               {"name":"Cybersecurity and Information Protection"},
               {"name":"Telecommunications and Radio Engineering"},
               {"name":"Automation and Computer-Integrated Technologies"}]

    return random.choice(courses)

@allure.step("get_course")
def get_course():
    course = random_course()
    return course

