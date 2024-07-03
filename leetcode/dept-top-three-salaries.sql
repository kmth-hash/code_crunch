-- https://leetcode.com/problems/department-top-three-salaries/description/

select dname as Department , name as Employee , salary from (
    select e.name , e.salary , d.name as dname , dense_rank() over(partition by d.name order by salary desc) as rn from employee e 
    left join department d on e.departmentId=d.id order by d.name
) temp where rn<=3 ;
-- order by Department desc, salary desc;
