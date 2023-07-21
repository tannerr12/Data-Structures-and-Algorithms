# Write your MySQL query statement below
select user_id, max(time_stamp) As last_stamp from Logins where YEAR(time_stamp) = 2020 Group by 1