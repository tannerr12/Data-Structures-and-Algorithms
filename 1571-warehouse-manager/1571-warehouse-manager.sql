# Write your MySQL query statement below
SELECT 
    w.name AS warehouse_name, 
    sum(w.units * p.width * p.height * p.length) AS volume
FROM 
    Warehouse w
JOIN products p on w.product_id = p.product_id
GROUP BY warehouse_name;