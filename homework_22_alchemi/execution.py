import logging
from random import randint

logging.basicConfig(level=logging.INFO)

from homework_22_alchemi.alchemi_client import SQLAlchemyClient
from homework_22_alchemi.university import Courses, Students

import os

db_client: SQLAlchemyClient = SQLAlchemyClient(os.getenv("db_url"))

db_client.create_table(Courses)
db_client.create_table(Students)

db_client.add_student()
student = db_client.session.query(Students.name).filter_by(course_id=32)
logging.info(student)
student_update = db_client.session.query(Students).filter_by(id=randint(21, 40)).first()
student_update.name = "Dmytro Nedilko"
db_client.session.commit()
logging.info(student_update)
deleted_student = db_client.session.query(Students).filter_by(name="Dmytro Nedilko").first()
db_client.session.delete(deleted_student)
db_client.session.commit()
logging.info(deleted_student)

db_client.close_connection()
