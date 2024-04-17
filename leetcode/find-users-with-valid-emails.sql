-- https://leetcode.com/problems/find-users-with-valid-e-mails/description

select * from Users where mail REGEXP '^[a-zA-Z][a-z-A-Z0-9_.-]*@leetcode[.]com$';
