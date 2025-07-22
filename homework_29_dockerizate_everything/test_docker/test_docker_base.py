import pytest
from homework_22_alchemi.university import Courses, Students


@pytest.mark.usefixtures("db_client")
class TestStudentCRUD:

    def test_add_students(self, db_client):
        db_client.add_student()
        count = db_client.session.query(Students).count()
        assert count > 0

    def test_get_students_by_course_id(self, db_client):
        course = db_client.session.query(Courses).first()
        assert course is not None, "No course found"

        students = db_client.session.query(Students.name).filter_by(course_id=course.id).all()
        assert isinstance(students, list)

    def test_update_student_name(self, db_client):
        student = db_client.session.query(Students).first()
        assert student is not None, "No student found in range"
        student.name = "Dmytro Nedilko"
        db_client.session.commit()

        updated = db_client.session.query(Students).filter_by(name="Dmytro Nedilko").first()
        assert updated is not None

    def test_delete_student_by_name(self, db_client):
        student = db_client.session.query(Students).filter_by(name="Dmytro Nedilko").first()
        assert student is not None, "Student to delete not found"
        db_client.session.delete(student)
        db_client.session.commit()

        deleted = db_client.session.query(Students).filter_by(name="Dmytro Nedilko").first()
        assert deleted is None
