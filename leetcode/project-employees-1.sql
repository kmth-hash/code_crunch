-- https://leetcode.com/problems/project-employees-i/?envType=study-plan-v2&envId=top-sql-50


select p.project_id , round(avg(e.experience_years) ,2) as average_years from Project p left join Employee e on p.employee_id=e.employee_id group by p.project_id ;
