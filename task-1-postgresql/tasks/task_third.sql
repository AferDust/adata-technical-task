WITH avg_all_salary AS (
    SELECT AVG(amount) AS avg_salary
    FROM salaries
    WHERE is_active = True
)

SELECT p.name AS Должность,
	ROUND(AVG(s.amount), 2) AS Средняя_ЗП_по_должности,
    CASE WHEN AVG(s.amount) > (SELECT avg_salary FROM avg_all_salary) THEN 'Да' ELSE 'Нет' END AS Больше_ли_общей_средней
FROM positions p
	JOIN salaries s ON p.id = s.position_id
WHERE s.is_active = True
GROUP BY p.name;
