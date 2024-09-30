import logging

from psycopg2 import DatabaseError

from connection import create_connection


def create_table(conn, sql_expression):
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as err:
        logging.error(err)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    sql_create_students = """CREATE TABLE IF NOT EXISTS students (
     id SERIAL PRIMARY KEY,
     name VARCHAR(120) NOT NULL,
     group_id INT,
     FOREIGN KEY (group_id) REFERENCES groups (id) ON DELETE SET NULL ON UPDATE CASCADE
    );"""

    sql_create_group = """CREATE TABLE IF NOT EXISTS groups (
         id SERIAL PRIMARY KEY,
         name VARCHAR(120) NOT NULL
        );"""

    sql_create_lecturer = """CREATE TABLE IF NOT EXISTS lecturers (
         id SERIAL PRIMARY KEY,
         name VARCHAR(120) NOT NULL
        );"""

    sql_create_subjects = """CREATE TABLE IF NOT EXISTS subjects (
         id SERIAL PRIMARY KEY,
         name VARCHAR(120) NOT NULL,
         lecturer_id INT,
         FOREIGN KEY (lecturer_id) REFERENCES lecturers (id) ON DELETE SET NULL ON UPDATE CASCADE
        );"""

    sql_create_students_grades = """CREATE TABLE IF NOT EXISTS students_grades (
         id SERIAL PRIMARY KEY,
         grade_value INT,
         student_id INT NOT NULL,
         subject_id INT NOT NULL,
         FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE ON UPDATE CASCADE,
         FOREIGN KEY (subject_id) REFERENCES subjects (id) ON DELETE CASCADE ON UPDATE CASCADE,
         date DATE NOT NULL
        );"""

    try:
        with create_connection() as conn:
            if conn is not None:
                # create_table(conn, sql_create_group)
                # create_table(conn, sql_create_students)
                # create_table(conn, sql_create_lecturer)
                # create_table(conn, sql_create_subjects)
                # create_table(conn, sql_create_students_grades)
                logging.info("the table is created")
            else:
                logging.error('Error: can\'t create the database connection')
    except RuntimeError as err:
        logging.error(err)
