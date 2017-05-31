from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

metadata = MetaData()
Base = declarative_base()
"""A definition of the database data of the application"""

# Create an engine that stores data in the database
engine = create_engine('sqlite:///school_db.db')


class Tutor(Base):
    """User model - a user ia a tutor/teacher"""
    __tablename__ = 'tutors'
    # Here we define columns for the table student
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(8), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Darasa(Base):
    """A list of all the available classes"""
    __tablename__ = 'madarasa'
    id = Column(Integer, primary_key=True)
    class_name = Column(String(20), nullable=False)
    status = Column(Boolean, default=False, nullable=False)
    # student_name = Column(String(20),nullable=True )
    # start_time = Column(DateTime(), default=datetime.now,nullable=True)

    students = relationship("Student", backref='madarasa', lazy='dynamic')
    # end_time =


class Student(Base):
    """Students model"""
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    student_name = Column(String(50), nullable=False)
    in_session = Column(Boolean, default=False)


    # 1-many relationship
    darasa_id = Column(Integer, ForeignKey('madarasa.id'))

# class CheckOut(Base):
#     """Checkout model"""
#     student_name = Column(String(20), nullable=False)
#     student_id = Column(String(5))
#     reason = Column(String(100), nullable=False)





# Create all tables in the engine database if they don't exist.
Base.metadata.create_all(engine)
