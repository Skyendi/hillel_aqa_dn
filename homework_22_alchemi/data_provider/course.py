from random import choice, random
import random


def random_course():

    courses = [{"name": "Software Engineering"},
               {"name":"Computer Networks and the Internet"},
               {"name":"Cybersecurity and Information Protection"},
               {"name":"Telecommunications and Radio Engineering"},
               {"name":"Automation and Computer-Integrated Technologies"}]

    return random.choice(courses)


def get_course():
    course = random_course()
    return course

#print(get_course())