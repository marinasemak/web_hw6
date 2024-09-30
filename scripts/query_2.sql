select s.name, round(avg(sg.grade_value), 0) as average_grade, sb.name as subject
from students s 
join students_grades sg on s.id = sg.student_id 
join subjects sb on sg.subject_id = sb.id
where sb.name = 'Geophysics'
group by s.name, sb.name 
order by average_grade desc
limit 1;