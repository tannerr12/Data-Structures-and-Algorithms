# Write your MySQL query statement below
select min(ABS(p.x - b.x)) as shortest from point p join point b on p.x != b.x