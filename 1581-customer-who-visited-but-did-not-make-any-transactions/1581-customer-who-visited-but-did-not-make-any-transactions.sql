# Write your MySQL query statement below

select v.customer_id,(select count(visit_id) as visits from Visits where visit_id not in (select visit_id from Transactions) and customer_id = v.customer_id) as count_no_trans from visits v group by customer_id having count_no_trans > 0