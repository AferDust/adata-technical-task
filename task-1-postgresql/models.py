from sqlalchemy import ForeignKey, String, Integer, Numeric, Boolean, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    department_positions: Mapped["DepartmentPosition"] = relationship("DepartmentPosition", back_populates="department")


class Position(Base):
    __tablename__ = "positions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    department_positions: Mapped["DepartmentPosition"] = relationship("DepartmentPosition", back_populates="position")
    salaries: Mapped["Salary"] = relationship("Salary", back_populates="position")


class DepartmentPosition(Base):
    __tablename__ = "department_positions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id", ondelete="CASCADE"))
    position_id: Mapped[int] = mapped_column(ForeignKey("positions.id", ondelete="CASCADE"))

    department: Mapped["Department"] = relationship("Department", back_populates="department_positions")
    position: Mapped["Position"] = relationship("Position", back_populates="department_positions")


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)

    salary: Mapped["Salary"] = relationship("Salary", back_populates="employee", uselist=False)


class Salary(Base):
    __tablename__ = "salaries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id", ondelete="CASCADE"))
    position_id: Mapped[int] = mapped_column(ForeignKey("positions.id", ondelete="SET NULL"))
    amount: Mapped[Numeric] = mapped_column(Numeric, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    start_date: Mapped[Date] = mapped_column(Date, nullable=False)
    end_date: Mapped[Date] = mapped_column(Date, nullable=True)

    employee: Mapped["Employee"] = relationship("Employee", back_populates="salary")
    position: Mapped["Position"] = relationship("Position", back_populates="salaries")
