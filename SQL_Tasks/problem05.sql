#problem link - https://www.hackerrank.com/challenges/more-than-75-marks/problem

#for DB2
select name from students where marks>75 order by substr(name,length(name)-2,3) ASC,id ASC;

#for MYsql
select name from students where marks>75 order by right(name,3) ASC, id ASC;

