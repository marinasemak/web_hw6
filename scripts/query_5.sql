select l.name as lecturer_name, sb.name as subjects_name
from lecturers l 
join subjects sb on l.id = sb.lecturer_id
where l.name = 'Christopher Benson';





