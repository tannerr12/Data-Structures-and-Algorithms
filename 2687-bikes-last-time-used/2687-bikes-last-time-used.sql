# Write your MySQL query statement below
select b.bike_number, end_time from bikes b where end_time = (select max(end_time) from bikes where bike_number = b.bike_number) group by bike_number