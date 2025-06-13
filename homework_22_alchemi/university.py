from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from homework_22_alchemi.declarative_base import Base


class Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    students = relationship("Students", back_populates="courses")


class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    course_id = Column(Integer, ForeignKey("courses.id"))

    courses = relationship("Courses", back_populates="students")
