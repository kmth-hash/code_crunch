-- https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true

select  ceil(  avg(salary) - avg( CAST( REPLACE( cast(salary as CHAR) , '0' , '' ) as UNSIGNED ) )  ) as salary from employees ;
