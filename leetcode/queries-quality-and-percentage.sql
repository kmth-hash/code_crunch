-- https://leetcode.com/problems/queries-quality-and-percentage/?envType=study-plan-v2&envId=top-sql-50

select query_name , round(  sum(rating /position) /count(query_name)  , 2) as quality, round( sum(case when rating<3 then 1 else 0 end )/count(query_name)*100 ,2) as poor_query_percentage  from Queries group by query_name  having query_name is not null ;
