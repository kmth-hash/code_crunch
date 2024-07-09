-- https://leetcode.com/problems/employees-with-missing-information/description/

select * from (
    select employee_id from Employees where employee_id not in (
    select Salaries.employee_id from Employees inner join Salaries on Salaries.employee_id=Employees.employee_id 
) 
union 
select employee_id from Salaries where employee_id not in (
    select Salaries.employee_id from Employees inner join Salaries on Salaries.employee_id=Employees.employee_id 
) 
)tbl order by employee_id asc ;
