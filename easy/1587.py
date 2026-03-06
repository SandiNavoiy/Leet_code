# Write your MySQL query statement below
select Users.name,sum(Transactions.amount) as balance from Users
INNER JOIN Transactions  on Transactions.account = Users.account
group by Users.name
having balance > 10000