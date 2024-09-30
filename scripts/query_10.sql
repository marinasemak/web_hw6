select distinct s.name, sb.name as subject, l.name as lecturer_name
from students s 
join students_grades sg on s.id = sg.student_id 
join subjects sb on sg.subject_id = sb.id
join lecturers l on l.id = sb.lecturer_id 
where s.name = 'Morgan Erickson' and l.name = 'Christopher Benson'
