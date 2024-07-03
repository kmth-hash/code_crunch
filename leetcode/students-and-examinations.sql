-- https://leetcode.com/problems/students-and-examinations/description/?envType=study-plan-v2&envId=top-sql-50

select s.* , b.*, count(e.student_id) as attended_exams from Students s cross join  Subjects b  left join Examinations e on e.subject_name =b.subject_name and s.student_id = e.student_id group by s.student_id , s.student_name, b.subject_name order by s.student_id , b.subject_name;
