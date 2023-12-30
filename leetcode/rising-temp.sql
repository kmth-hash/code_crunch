-- https://leetcode.com/problems/rising-temperature/?envType=study-plan-v2&envId=top-sql-50

select r1.id as Id from Weather r1 join Weather r2 on r1.temperature>r2.temperature and datediff(r1.recordDate , r2.recordDate) = 1