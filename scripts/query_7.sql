select s.name, sg.grade_value, sb.name as subject, g."name" as group_name
from students s 
join students_grades sg on s.id = sg.student_id 
join subjects sb on sg.subject_id = sb.id
join "groups" g on s.group_id = g.id 
where sb.name = 'Geophysics' and g."name" = 'GroupC';

