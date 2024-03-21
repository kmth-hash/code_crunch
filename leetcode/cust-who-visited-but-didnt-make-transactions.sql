-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50

select customer_id , count(*) as count_no_trans from visits where visit_id not in (select visit_id from transactions ) group by customer_id ;
