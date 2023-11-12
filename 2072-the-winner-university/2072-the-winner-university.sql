SELECT CASE 
    WHEN (SELECT COUNT(student_id) FROM NewYork WHERE score >= 90) > 
         (SELECT COUNT(student_id) FROM California WHERE score >= 90) 
    THEN 'New York University'
    WHEN (SELECT COUNT(student_id) FROM NewYork WHERE score >= 90) < 
         (SELECT COUNT(student_id) FROM California WHERE score >= 90) 
    THEN 'California University'
    ELSE 'No Winner'
END AS winner;
