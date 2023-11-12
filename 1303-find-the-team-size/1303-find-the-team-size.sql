# Write your MySQL query statement below
select e.employee_id, (select count(team_id) from employee where team_id = e.team_id) as team_size from employee e  