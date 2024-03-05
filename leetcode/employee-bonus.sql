
/* https://leetcode.com/problems/employee-bonus/description/?envType=study-plan-v2&envId=top-sql-50 */

select a.name , b.bonus from Employee a left join Bonus b on a.empId=b.empId where b.bonus<1000 or b.bonus is NULL;

