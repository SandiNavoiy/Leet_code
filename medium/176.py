# Write your MySQL query statement below
SELECT (
    SELECT DISTINCT salary
    FROM employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;



выбираем и заворачиваем еще в один селект. чобы получить нулл