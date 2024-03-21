-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/?envType=study-plan-v2&envId=top-sql-50

-- # Write your MySQL query statement below
select e2.employee_id , e2.name , count(e1.employee_id) as reports_count , round(avg(e1.age)) as average_age from Employees e1 join Employees e2 on e1.reports_to=e2.employee_id group by e2.employee_id, e2.name order by e2.employee_id; 
