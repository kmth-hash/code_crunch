-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description

select id , sum(val) as num from (
    select accepter_id as id  ,count(accepter_id) as val from RequestAccepted group by accepter_id 
    union all 
    select requester_id as id ,count(requester_id) as val from RequestAccepted group by requester_id
) tmp group by id order by num desc limit 1;
