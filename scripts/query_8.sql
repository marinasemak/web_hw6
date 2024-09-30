select l.name as lecturer_name, sb.name as subjects_name, round(avg(sg.grade_value), 0) as average_grade
from lecturers l
join subjects sb on l.id = sb.lecturer_id
join students_grades sg on sb.id = sg.subject_id 
where l.name = 'Christopher Benson'
group by l."name", sb."name" ;
