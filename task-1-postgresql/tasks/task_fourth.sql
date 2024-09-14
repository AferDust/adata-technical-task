SELECT
	p.name AS Должность,
   	json_agg(DISTINCT d.name) AS Отделы,
    json_agg(DISTINCT e.first_name || ' ' || e.last_name) FILTER (WHERE s.start_date < '2021-01-01') AS Список_сотрудников_до_2021,
    ROUND(AVG(s.amount), 2) AS Средняя_ЗП
FROM positions p
	JOIN department_positions dp ON p.id = dp.position_id
	JOIN departments d ON dp.department_id = d.id
	JOIN salaries s ON p.id = s.position_id
	JOIN employees e ON s.employee_id = e.id
WHERE s.is_active = True
GROUP BY p.name;