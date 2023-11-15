# Write your MySQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary as Salary
From Employee e
JOIN Department d ON e.departmentId = d.id
WHERE(departmentId, salary) IN
(SELECT departmentId, max(salary) FROM Employee GROUP BY departmentId)