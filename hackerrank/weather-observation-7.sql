-- https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true

select DISTINCT CITY from Station where UPPER(SUBSTR(CITY , LENGTH(CITY),1)) in ('A',"E",'I','O','U') ; 
