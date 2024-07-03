-- https://leetcode.com/problems/department-highest-salary/description/?lang=pythondata

select d.name as Department , e.name as Employee, e.salary as Salary 
from Employee e Left join Department d on d.id=e.departmentId 
where (d.id , e.salary ) in (select departmentId , max(salary) from Employee group by departmentId);
