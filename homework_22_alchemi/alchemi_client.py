from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from homework_22_alchemi.data_provider.course import get_course
from homework_22_alchemi.data_provider.student import get_student
from homework_22_alchemi.university import Courses, Students

load_dotenv()


class SQLAlchemyClient:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.__engine = self.__create_engine()
        self.__session = self.__create_session()

    @property
    def session(self):
        return self.__session

    def __create_engine(self):

        return create_engine(self.db_url)

    def __create_session(self):

        session = sessionmaker(bind=self.__engine)
        return session()

    def create_table(self, table_obj):

        table_obj.metadata.create_all(self.__engine)

    def add_course(self):
        for _ in range(5):
            new_course_dict = get_course()

            existing_course = self.session.query(Courses).filter_by(name=new_course_dict["name"]).first()

            if existing_course:
                continue

            course = Courses(**new_course_dict)
            self.session.add(course)

        self.session.commit()

    def add_student(self):
        course_ids = [course.id for course in self.session.query(Courses).all()]
        for _ in range(20):
            new_student_dict = get_student(course_ids)
            student = Students(**new_student_dict)
            self.session.add(student)
        self.session.commit()

    def close_connection(self):

        self.__session.close()
