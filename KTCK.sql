#phần 2
# Câu 2

SELECT SUM(commission), city FROM salesman GROUP BY city



#câu 2b

select * from customer c
join salesman s on c.salesman_id = s.salesman_id
where s.commission > 0.12 
order by s.commission



