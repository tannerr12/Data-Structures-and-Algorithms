# Write your MySQL query statement below
select project_id from project group by project_id having Count(employee_id) >= ALL(SELECT COUNT(employee_id) FROM Project GROUP BY project_id)