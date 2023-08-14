# Write your MySQL query statement below

SELECT e.employee_id, 
       CASE WHEN e.name NOT LIKE 'M%' AND e.employee_id % 2 = 1 THEN e.salary 
            ELSE 0 
       END AS bonus
FROM employees e order by employee_id
