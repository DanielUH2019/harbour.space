"""Problem 07: Create and read data with SQLAlchemy.

Task:
1. Open a SQLAlchemy Session on `school.db`.
2. Create one Assignment for an existing student.
3. Read all students.
4. Read students with age >= 22 sorted by age descending.
5. Read assignments with joined student names.

Starter:
- Reuse `Student` and `Assignment` from `db_models.py`.
- Use `select(...)` queries.
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from db_models import Assignment, Student
import uuid
DB_URL = "sqlite:///school.db"


def main() -> None:
    engine = create_engine(DB_URL, echo=False)
    count = 0
    with Session(engine) as session:
        # TODO 1: add an assignment for an existing student
        random_student = select(Student)
        random_student = session.scalar(random_student)
        print("random student: ", random_student)
        print()
        assignment = Assignment(id=8, title=f"tittle{count}", score=count, student_id = random_student.id )
        session.add(assignment)
        # TODO 2: read all students
        students = select(Student)
        students = session.scalars(students).all()
        print("students ", students)
        print()
        # TODO 3: read filtered + sorted students
        sorted_students = select(Student).where(Student.age > 20).order_by(Student.age)
        sorted_students = session.scalars(sorted_students).all()
        print("sorted students: ", sorted_students)
        print()
        # TODO 4: read assignments with student data
        assignments = select(Assignment)
        assignments = session.scalars(assignments).all()
        print("assignments: ", assignments)
        print()
        session.commit()


if __name__ == "__main__":
    main()
