select g."name" as group_name, round(avg(sg.grade_value), 0) as average_grade, sb.name as subject
from students s 
join students_grades sg on s.id = sg.student_id 
join subjects sb on sg.subject_id = sb.id
join "groups" g on s.group_id = g.id 
where sb.name = 'Mathematics'
group by s.group_id, sb.name, g."name" 
order by average_grade desc
limit 1;