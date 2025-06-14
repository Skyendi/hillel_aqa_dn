import logging
logging.basicConfig(level=logging.INFO)

from homework_22_alchemi.alchemi_client import SQLAlchemyClient
from homework_22_alchemi.university import Courses, Students
from homework_22_alchemi.data_provider.student import get_student
from homework_22_alchemi.data_provider.course import get_course
import os

db_client: SQLAlchemyClient = SQLAlchemyClient(os.getenv("db_url"))

db_client.create_table(table_obj=Courses)
db_client.create_table(table_obj=Students)

for _ in range(5):

    new_course_dict = get_course()
    course = Courses(**new_course_dict)
    db_client.session.add(course)
db_client.session.commit()

for _ in range(20):
    new_student_dict = get_student()
    student = Students(**new_student_dict)
    db_client.session.add(student)
db_client.session.commit()

student = db_client.session.query(Students.name).filter_by(course_id=10)
logging.info(student)
student_update = db_client.session.query(Students).filter_by(id=45).first()
student_update.name = "Dima Ned"
db_client.session.commit()
logging.info(student_update)
deleted_student = db_client.session.query(Students).filter_by(id=45).first()
db_client.session.delete(deleted_student)
db_client.session.commit()
logging.info(deleted_student)

db_client.close_connection()
