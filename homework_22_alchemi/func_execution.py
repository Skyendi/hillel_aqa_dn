import logging
import os
from homework_22_alchemi.alchemi_client import SQLAlchemyClient
from homework_22_alchemi.university import Courses, Students
from homework_22_alchemi.data_provider.student import get_student
from homework_22_alchemi.data_provider.course import get_course

logging.basicConfig(level=logging.INFO)


def init_db() -> SQLAlchemyClient:
    db_url = os.getenv("db_url")
    if not db_url:
        raise ValueError("Environment variable 'db_url' is not set.")

    db_client = SQLAlchemyClient(db_url)
    db_client.create_table(Courses)
    db_client.create_table(Students)
    return db_client


# def populate_courses(db_client: SQLAlchemyClient, count: int = 5):
#
#     for _ in range(count):
#         course_data = get_course()
#         course = Courses(**course_data)
#         db_client.session.add(course)
#     db_client.session.commit()
#     logging.info(f"{count} courses inserted.")


def populate_students(db_client: SQLAlchemyClient, count: int = 20):
    for _ in range(count):
        student_data = get_student()
        student = Students(**student_data)
        db_client.session.add(student)
    db_client.session.commit()
    logging.info(f"{count} students inserted.")


def get_students_by_course(db_client: SQLAlchemyClient, course_id: int):
    students = db_client.session.query(Students.name).filter_by(course_id=course_id).all()
    for s in students:
        logging.info(f"Student in course {course_id}: {s.name}")


def update_student_name(db_client: SQLAlchemyClient, student_id: int, new_name: str):
    student = db_client.session.query(Students).filter_by(id=student_id).first()
    if student:
        student.name = new_name
        db_client.session.commit()
        logging.info(f"Updated student: {student}")
    else:
        logging.warning(f"Student with ID={student_id} not found.")


def delete_student(db_client: SQLAlchemyClient, student_id: int):
    student = db_client.session.query(Students).filter_by(id=student_id).first()
    if student:
        db_client.session.delete(student)
        db_client.session.commit()
        logging.info(f"Deleted student: {student}")
    else:
        logging.warning(f"Student with ID={student_id} not found.")


def delete_all_students(db_client: SQLAlchemyClient):
    students = db_client.session.query(Students).all()
    if students:
        for student in students:
            db_client.session.delete(student)
        db_client.session.commit()
        logging.info(f"🗑️ {len(students)} students deleted.")
    else:
        logging.info("🧹 No students to delete.")


def main():
    db_client = init_db()
    try:
        # populate_courses(db_client)
        populate_students(db_client)
        get_students_by_course(db_client, course_id=11)
        update_student_name(db_client, student_id=42, new_name="Dima Ned")
        delete_student(db_client, student_id=42)
    finally:
        db_client.close_connection()


if __name__ == "__main__":
    main()
