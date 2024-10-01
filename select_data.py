from connection import create_connection
from psycopg2 import DatabaseError

def execute_query(sql: str) -> list:
    with create_connection() as conn:
        if conn is not None:
            cur = conn.cursor()
            cur.execute(sql)
            return cur.fetchall()
        else:
            print('Error: can\'t create the database connection')
    except RuntimeError as err:
    logging.error(err)


sql = """
select s.name, round(avg(sg.grade_value), 0) as average_grade
from students s 
join students_grades sg on
s.id = sg.student_id 
group by s.name 
order by average_grade desc
limit 5;
"""

print(execute_query(sql))
