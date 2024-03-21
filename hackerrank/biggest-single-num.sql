-- https://leetcode.com/problems/biggest-single-number/?envType=study-plan-v2&envId=top-sql-50

select CASE when count(num)=1 then num else null end as num from MyNumbers group by num  order by num DESC limit 1;
