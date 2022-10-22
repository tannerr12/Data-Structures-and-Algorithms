# Write your MySQL query statement below


select Department.name as "Department", Employee.name as "Employee",Salary from employee join Department ON Employee.DepartmentId = Department.id where (Employee.DepartmentId, Salary) IN (select DepartmentId, Max(Salary) from Employee Group by DepartmentId) 