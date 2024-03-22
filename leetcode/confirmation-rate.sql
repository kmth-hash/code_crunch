-- https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50

select s.user_id , round( case when c.conf is not null then c.conf else 0 end , 2) as confirmation_rate from Signups s left join ( 
    select user_id , sum( case when action='confirmed' then 1 else 0 end)/count(*) as conf from Confirmations group by user_id ) as c on s.user_id=c.user_id ;
