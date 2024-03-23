-- https://www.hackerrank.com/challenges/weather-observation-station-9/problem

select distinct city from station where city not in (
select CITY from Station where city LIKE 'a%' or city LIKE 'e%' or city LIKE 'i%' or city LIKE 'o%' or city LIKE 'u%'
);
