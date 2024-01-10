SELECT 
    ad_id, 
    COALESCE(
        ROUND(
            SUM(CASE WHEN action = 'Clicked' THEN 1 ELSE 0 END) / 
            NULLIF(
                SUM(CASE WHEN action IN ('Clicked', 'Viewed') THEN 1 ELSE 0 END),
                0
            ) * 100, 
            2
        ), 
        0.00
    ) AS ctr 
FROM 
    ads 
GROUP BY 
    ad_id 
ORDER BY 
    ctr DESC, 
    ad_id;
