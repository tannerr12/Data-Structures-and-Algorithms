SELECT 
    query_name, 
    IFNULL(ROUND(AVG(rating / position), 2), 0) AS quality, 
    ROUND(
        (COUNT(CASE WHEN rating < 3 THEN 1 END) / COUNT(*)) * 100, 
        2
    ) AS poor_query_percentage 
FROM 
    queries 
GROUP BY 
    query_name;
