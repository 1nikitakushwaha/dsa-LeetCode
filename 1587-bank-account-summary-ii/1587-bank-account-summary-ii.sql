# Write your MySQL query statement below
select u.name,
sum(t.amount) as balance
from Users u
right join Transactions t
on u.account=t.account
group by t.account
HAVING SUM(t.amount) > 10000;;
