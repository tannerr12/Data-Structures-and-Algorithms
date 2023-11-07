# Write your MySQL query statement below
select ABS((select max(salary) as salary from salaries where department = 'Engineering') - (select max(salary) as salary from salaries where department = 'Marketing')) as "salary_difference"

