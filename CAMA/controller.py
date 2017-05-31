

from .model import Tutor, Student, Darasa, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
from termcolor import cprint, colored

engine = create_engine('sqlite:///school_db.db')
# Bind the engine to the metadata of the Base class so that the
# models can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# Instance establishes all conversations with the database
session = DBSession()


def create_tutor(username, password):
    """Create a new user"""
    new_tutor = Tutor(username=username, password=password)
    session.add(new_tutor)
    session.commit()
    cprint("Created new user:", 'green', 'on_grey')
    cprint("\tName: {0}".format(new_tutor.username, 'cyan'))

def login(username, password):
    new_login = session.query(Tutor)


def create_student(student_name):
    """Create a new student"""
    new_student = Student(student_name=student_name)
    session.add(new_student)
    session.commit()
    cprint("Created new student:", 'green', 'on_grey')
    cprint("\tId: {0}\n\tName: {1}".format(
        new_student.id, new_student.student_name), 'cyan')


def create_darasa(class_name):
    new_class = Darasa(class_name=class_name)
    session.add(new_class)
    session.commit()
    cprint("Class added successfully:", 'green', 'on_grey')
    cprint("\tId: {0}\n\tName: {1}".format(
        new_class.id, new_class.class_name), 'cyan')


def list_of_students():
    wanafunzi = session.query(Student)

    counts = []
    for s in wanafunzi:
        student = [s.id, s.student_name, s.in_session]
        counts.append(student)
    length = len(counts)
    if length > 0:
        if length > 1:
            print(colored('\n' + '\t   All Student(' + str(length) + ')', 'green', attrs=['bold']))
            print(colored(tabulate(counts,
                                   headers=['Student Id', 'Student Name', 'Status '],
                                   tablefmt='fancy_grid'), 'cyan'))
        else:
            print(colored('\n\t   ' + str(length) + ' students found\n', 'green', attrs=['bold']))
            print(colored(tabulate(counts,
                                   headers=['First Name', 'Last Name', 'In Session'],
                                   tablefmt='fancy_grid'), 'cyan'))
    else:
        print(colored("There are no students Please add", "red"))


def list_of_classes():
    class_list = session.query(Darasa)

    counts = []
    for s in class_list:
        my_class = [s.id, s.class_name, s.status]
        counts.append(my_class)
    length = len(counts)
    if length > 0:
        if length > 1:
            print(colored('\n' + '\t   All available classes(' + str(length) + ')', \
                          'green', attrs=['bold']))
            print(colored(tabulate(counts, \
                                   headers=['Class Id', 'Class Name', 'Status'], \
                                   tablefmt='fancy_grid'), 'cyan'))
        else:
            print(colored('\n\t   ' + str(length) + ' class found\n', 'green', attrs=['bold']))
            print(colored(tabulate(counts, \
                                   headers=['Class Id', 'Class Name', 'Status'], \
                                   tablefmt='fancy_grid'), 'cyan'))
    else:
        print(colored("There are no classes added", "red"))


def anza_darasa(class_to_start):
    class_list = session.query(Darasa).filter_by(class_name=class_to_start).first()
    class_list.status = True
    session.commit()
    cprint("{} class will start right away".format(class_to_start), 'cyan')


def check_in_student(student_id, class_name):
    """check in a student to a class with their ID supplied"""
    class_id = session.query(Darasa).filter_by(class_name=class_name).first()
    # that_class = class_id.class_name
    if class_id.status == False:
        cprint("That session is not started", 'white', 'on_red')
    else:
        student_list = session.query(Student).filter_by(id=student_id).first()
        if student_list.in_session == True:
            cprint("That student is in another session", 'white', 'on_red')
        else:
            student_list.in_session = True
            session.commit()
            cprint('Student added in session', 'cyan')


def maliza_darasa(class_to_end):
    class_list = session.query(Darasa).filter_by(class_name=class_to_end).first()
    if class_list.status == False:
        cprint("That session is not started", 'white', 'on_red')
    else:
        class_list.status = False
        session.commit()
        cprint("{} Session has ended".format(class_to_end), 'cyan')
