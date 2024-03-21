-- https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true

select CITY , LENGTH(CITY) from station order by LENGTH(CITY),CITY LIMIT 1;
select CITY , LENGTH(CITY) from station order by LENGTH(CITY) DESC ,CITY DESC LIMIT 1;
