-- https://leetcode.com/problems/tree-node/description/

select id , 
case 
    when p_id is null then 'Root' 
    when p_id in (select t2.id from tree t2) and id in (select t3.p_id from tree t3) then 'Inner'
    else 'Leaf'
end as type 
from tree ;
