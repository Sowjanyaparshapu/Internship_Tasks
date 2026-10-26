# problem link - https://www.hackerrank.com/challenges/weather-observation-station-3/problem

select DISTINCT city from station where mod(id,2)=0; #for DB2 it will work
# select DISTINCT city from station where id%2=0; for mysql it will work
