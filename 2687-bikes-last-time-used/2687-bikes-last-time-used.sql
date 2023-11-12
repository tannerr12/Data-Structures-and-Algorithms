# Write your MySQL query statement below
select b.bike_number, max(end_time) as end_time from bikes b group by bike_number