import logging
import random

from faker import Faker

from datetime import date
from random import randint
from psycopg2 import DatabaseError

from connection import create_connection


def delete_task(conn):

    sql = 'DELETE FROM students_grades'
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except DatabaseError as err:
        logging.error(err)
        conn.rollback()
    finally:
        cur.close()



if __name__ == '__main__':
    with create_connection() as conn:
        delete_task(conn)

