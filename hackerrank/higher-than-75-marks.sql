-- https://www.hackerrank.com/challenges/more-than-75-marks/problem?isFullScreen=true


select name from Students where marks > 75 order by substr(name,-3) asc, id asc;
