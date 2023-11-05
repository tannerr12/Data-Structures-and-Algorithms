# Write your MySQL query statement below
SELECT seller_id
FROM Sales
GROUP BY seller_id
HAVING SUM(PRICE) >= all (
    SELECT SUM(PRICE)
    FROM Sales
    GROUP BY seller_id
)