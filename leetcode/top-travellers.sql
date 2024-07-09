-- https://leetcode.com/problems/top-travellers/description/

select name , COALESCE(sum(distance) , 0) as 'travelled_distance' from (
select  u.id , coalesce(distance,0) as distance,u.name from Rides r right join Users u on u.id=r.user_id
) tbl group by id  order by travelled_distance desc , length(name)  desc ;

