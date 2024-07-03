-- https://leetcode.com/problems/list-the-products-ordered-in-a-period/description/

select p.product_name , sum(o.unit) as unit from Products p left join Orders o on p.product_id=o.product_id where month(order_date)=2 and year(order_date)=2020 group by o.product_id having unit>=100;
