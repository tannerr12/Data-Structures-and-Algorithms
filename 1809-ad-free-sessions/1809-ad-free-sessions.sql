# Write your MySQL query statement below

select session_id from playback p where (select count(timestamp) from ads where customer_id = p.customer_id and timestamp >= p.start_time and timestamp <= p.end_time) = 0