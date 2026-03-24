"""Shared SQLAlchemy ORM models for Problems 06-07.

Task:
- Keep Student mapped to existing `students` table.
- Add Assignment as related model (many assignments per student).
- Complete relationship fields in both models.
"""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    track: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Student(id={self.id}, name={self.name}, age={self.age}, email={self.email}, track={self.track})"