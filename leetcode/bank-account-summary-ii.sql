-- https://leetcode.com/problems/bank-account-summary-ii/

select name, sum(amount) as BaLANCE from Transactions left join Users on Users.account=Transactions.account group by Transactions.account having sum(amount)>10000;
