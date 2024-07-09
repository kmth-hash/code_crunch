-- https://leetcode.com/problems/the-latest-login-in-2020/description/

select user_id , max(time_stamp) as last_stamp from Logins where user_id in (
    select distinct user_id from Logins where year(time_stamp)=2020
) and year(time_stamp)=2020 group by user_id ;
