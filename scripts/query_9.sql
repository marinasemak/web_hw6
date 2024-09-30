select distinct s.name, sb.name as subject
from students s 
join students_grades sg on s.id = sg.student_id 
join subjects sb on sg.subject_id = sb.id
where s.name = 'Morgan Erickson'


