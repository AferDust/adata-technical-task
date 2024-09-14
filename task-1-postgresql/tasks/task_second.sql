SELECT
	d.name AS Отдел,
	ROUND(AVG(salaries.amount), 2) AS Средняя_заработная_плата
FROM departments d
	JOIN department_positions dp ON d.id = dp.department_id
	JOIN positions p ON dp.position_id = p.id
	JOIN salaries ON p.id = salaries.position_id
WHERE salaries.is_active = True
GROUP BY d.name;
