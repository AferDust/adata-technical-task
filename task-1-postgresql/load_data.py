import os
import pandas as pd
import numpy as np

from src.models import Department, Position, Employee, Salary, DepartmentPosition
from src.database import get_db_session

data_folder = 'data'

departments_df = pd.read_csv(os.path.join(data_folder, 'departments.csv'))
positions_df = pd.read_csv(os.path.join(data_folder, 'positions.csv'))
employees_df = pd.read_csv(os.path.join(data_folder, 'employees.csv'))
department_positions_df = pd.read_csv(os.path.join(data_folder, 'department_positions.csv'))
salaries_df = pd.read_csv(os.path.join(data_folder, 'salaries.csv'))


with get_db_session() as session:
    for _, row in departments_df.iterrows():
        department = Department(id=row['id'], name=row['name'])
        session.add(department)

    for _, row in positions_df.iterrows():
        position = Position(id=row['id'], name=row['name'])
        session.add(position)

    for _, row in employees_df.iterrows():
        employee = Employee(id=row['id'], first_name=row['first_name'], last_name=row['last_name'])
        session.add(employee)

    for _, row in department_positions_df.iterrows():
        department_position = DepartmentPosition(id=row['id'], department_id=row['department_id'], position_id=row['position_id'])
        session.add(department_position)

    salaries_df['end_date'] = salaries_df['end_date'].replace({np.nan: None})
    for _, row in salaries_df.iterrows():
        salary = Salary(
            employee_id=row['employee_id'],
            position_id=row['position_id'],
            amount=row['amount'],
            is_active=row['is_active'],
            start_date=row['start_date'],
            end_date=row['end_date']
        )
        session.add(salary)
