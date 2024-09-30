import logging

from faker import Faker

from datetime import date
from random import randint
from psycopg2 import DatabaseError

from connection import create_connection

fake = Faker()
STUDENTS_COUNT = 50
GROUPS_COUNT = 3
LECTURER_COUNT = 5
SUBJECTS_COUNT = 5
fake_data = Faker()


def generate_fake_data(number_students, number_lecturers) -> tuple():
    fake_students = []
    fake_groups = ["GroupA", "GroupB", "GroupC"]
    fake_lecturers = []
    fake_subjects = ["Geology", "Geography", "Chemistry", "Geophysics", "Mathematics"]

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_lecturers):
        fake_lecturers.append(fake_data.name())

    return fake_groups, fake_students, fake_lecturers, fake_subjects


def prepare_data(groups, students, lecturers, subjects) -> tuple():
    for_students = []

    for student in students:
        for_students.append((student, randint(1, GROUPS_COUNT)))

    for_groups = []

    for group in groups:
        for_groups.append((group,))

    for_lecturers = []

    for lect in lecturers:
        for_lecturers.append((lect,))

    for_subjects = []

    for subj in subjects:
        for_subjects.append((subj, randint(1, LECTURER_COUNT)))

    for_grades = []
    start_date = date(2023, 9, 1)
    end_date = date(2024, 6, 30)

    for student in range(1, STUDENTS_COUNT + 1):
        for _ in range(1, 20):
            for_grades.append((randint(60, 100), student, randint(1, SUBJECTS_COUNT),
                               fake_data.date_between(start_date, end_date)))

    return for_groups, for_students, for_lecturers, for_subjects, for_grades

def insert_data(conn, data, sql_expression):
    cur = conn.cursor()
    try:
        cur.executemany(sql_expression, data)
        conn.commit()
    except DatabaseError as err:
        logging.error(err)
        conn.rollback()
    finally:
        cur.close()



if __name__ == '__main__':
    groups, students, lecturers, subjects, grades = prepare_data(*generate_fake_data(STUDENTS_COUNT, LECTURER_COUNT))
    sql_to_groups = "INSERT INTO groups(name) VALUES(%s)"
    sql_to_students = "INSERT INTO students(name, group_id) VALUES(%s, %s)"
    sql_to_lecturers = "INSERT INTO lecturers(name) VALUES(%s)"
    sql_to_subjects = "INSERT INTO subjects(name, lecturer_id) VALUES(%s, %s)"
    sql_to_grades = "INSERT INTO students_grades(grade_value, student_id, subject_id, date) VALUES(%s, %s, %s, %s)"
    try:
        with create_connection() as conn:
            if conn is not None:
                # insert_data(conn, groups, sql_to_groups)
                # insert_data(conn, students, sql_to_students)
                # insert_data(conn, lecturers, sql_to_lecturers)
                # insert_data(conn, subjects, sql_to_subjects)
                insert_data(conn, grades, sql_to_grades)
            else:
                print('Error: can\'t create the database connection')
    except RuntimeError as err:
        logging.error(err)
