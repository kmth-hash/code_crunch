-- https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true

select 
case 
    when a+b>c and a+c>b and b+c>a then 
        case 
            when a=b and a=c and b=c then 'Equilateral' 
            when A=B OR A=C OR B=C then 'Isosceles' 
            else 'Scalene' 
        end
    else 'Not A Triangle' 
end as res from triangles;
