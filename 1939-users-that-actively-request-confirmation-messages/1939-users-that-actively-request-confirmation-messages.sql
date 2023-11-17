SELECT DISTINCT c1.user_id
FROM Confirmations c1
JOIN Confirmations c2 ON c1.user_id = c2.user_id AND c1.time_stamp < c2.time_stamp
WHERE TIMESTAMPDIFF(SECOND, c1.time_stamp, c2.time_stamp) <= 86400
