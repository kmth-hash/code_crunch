-- https://leetcode.com/problems/fix-names-in-a-table/description/?envType=study-plan-v2&envId=top-sql-50

-- # Write your MySQL query statement below
select user_id , concat(upper(substr(name,1,1)),lower(substr(name,2))) as name from Users order by user_id;