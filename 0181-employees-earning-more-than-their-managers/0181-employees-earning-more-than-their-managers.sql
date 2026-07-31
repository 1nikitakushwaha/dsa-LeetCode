# Write your MySQL query statement below
Select E.name AS Employee
FROM Employee AS E
JOIN Employee AS M
ON E.managerId=M.id
WHERE E.salary>M.salary;