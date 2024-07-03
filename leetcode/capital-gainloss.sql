-- https://leetcode.com/problems/capital-gainloss/description/

select stock_name , sum(if(operation = 'sell' , price , -price)) as capital_gain_loss from  Stocks group by stock_name ;
