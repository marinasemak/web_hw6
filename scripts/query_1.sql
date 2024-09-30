select s.name, round(avg(sg.grade_value), 0) as average_grade
from students s 
join students_grades sg on
s.id = sg.student_id 
group by s.name 
order by average_grade desc
limit 5;


