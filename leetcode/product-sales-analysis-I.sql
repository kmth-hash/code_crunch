
# https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50

Select p.product_name , s.year , s.price from Sales s left outer Join Product p on p.product_id=s.product_id ;
