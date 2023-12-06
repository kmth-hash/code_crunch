select departmentName AS "Department Name",count(course.deptid) as "Number of Courses"
from department
join course on course.deptid=department.id
group by department.departmentName
order by "Number of Courses" ,"Department Name" ASC;


select course.courseName AS "Course Name",count(StudentCourse.courseid) as "Number of Students" 
from course
join StudentCourse on course.id=StudentCourse.courseid
group by course.courseName
order by "Number of Students" DESC , "Course Name" ASC;


