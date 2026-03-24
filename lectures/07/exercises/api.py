from unittest import result
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from db_models import Student
import sqlite3


# Note: deployed on https://harbour-space.onrender.com using the dockerfile

DB_URL = "sqlite:///school.db"

app = FastAPI()

class StudentCreateModel(BaseModel):
    name: str
    age: int 
    email: str
    track: str

class StudentModel(BaseModel):
    id: int 
    name: str
    age: int 
    email: str
    track: str



def main():
    database = 'school.db'
    create_table = "CREATE TABLE IF NOT EXISTS students ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, email TEXT UNIQUE NOT NULL, track TEXT NOT NULL )"

    try:
        with sqlite3.connect(database) as conn:
            cursor = conn.cursor()
            cursor.execute(create_table)   
            conn.commit()

    except sqlite3.OperationalError as e:
        print(e)

@app.get("/")
def get_all_students() -> list[StudentModel]:
    # TODO: return your health payload
    engine = create_engine(DB_URL, echo=False)
    results = []
    with Session(engine) as session:
        students = select(Student)
        students = session.scalars(students).all()
        for s in students:
            results.append(StudentModel(id=s.id, name=s.name, age=s.age, email=s.email, track=s.track))
    return results

@app.get(f"/{id}")
def get_by_id(id: int) -> StudentModel:
    engine = create_engine(DB_URL, echo=False)

    with Session(engine) as session:
        s = select(Student).where(Student.id == id)
        s = session.scalar(s)
        if not s:
            raise HTTPException(status_code=404)
        result = StudentModel(id=s.id, name=s.name, age=s.age, email=s.email, track=s.track)

    return result


@app.post("/")
def create_student(data: StudentCreateModel) -> StudentModel:
    global STUDENT_COUNTER
    engine = create_engine(DB_URL, echo=False)
    new_id = None
    with Session(engine) as session:
        student = Student(**data.model_dump())
        session.add(student)
        session.commit()
        new_id = student.id
    
    return StudentModel(id=new_id, **data.model_dump())


if __name__ == "__main__":
    main()