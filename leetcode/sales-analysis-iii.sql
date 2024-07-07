-- https://leetcode.com/problems/sales-analysis-iii/description/

select tbl.product_id, product_name from ( select p.product_id, product_name,sale_date from 
Product p left join Sales s on p.product_id = s.product_id
group by p.product_id having sale_date between '2019-01-01' and '2019-03-31') tbl ;
