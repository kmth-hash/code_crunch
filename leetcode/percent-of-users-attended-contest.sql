-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/

select contest_id ,round( count(user_id)/(select count(*) from Users)*100 ,2) as percentage from register group by contest_id order by percentage desc ,contest_id ASC;
