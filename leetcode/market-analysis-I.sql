-- https://leetcode.com/problems/market-analysis-i/description/

select user_id as buyer_id , join_date , count(order_id) as orders_in_2019
from Orders RIGHT JOIN Users 
on Orders.buyer_id=Users.user_id
and year(Orders.order_date)=2019 
group by user_id; 
