SELECT
    employees.first_name ||' '|| employees.last_name AS ФИО,
	salaries.amount AS Заработная_плата,
	positions.name AS Должность
FROM employees
	JOIN salaries ON employees.id = salaries.employee_id
	JOIN positions ON salaries.position_id = positions.id
	JOIN department_positions dp ON positions.id = dp.position_id
	JOIN departments ON dp.department_id = departments.id
WHERE employees.first_name like 'Давид' AND departments.name = 'Снабжение' AND salaries.is_active = True;
