from fastapi import FastAPI, HTTPException
from typing import Optional
import schemas

app = FastAPI(
    title="Course Management API",
    description="FastAPI Course Management",
    version="1.0"
)

courses = []


@app.get("/")
def home():
    return {"message": "API running"}


@app.post("/api/courses/", response_model=schemas.CourseResponse)
async def create_course(course: schemas.CourseCreate):

    new_course = {
        "id": len(courses) + 1,
        **course.model_dump()
    }

    courses.append(new_course)

    return new_course


@app.get("/api/courses/")
async def get_courses(
        skip: int = 0,
        limit: int = 10,
        department_id: Optional[int] = None
):

    result = courses

    if department_id is not None:
        result = [
            c for c in result
            if c["department_id"] == department_id
        ]

    return result[skip:skip + limit]


@app.get("/api/courses/{course_id}")
async def get_course(course_id: int):

    for course in courses:
        if course["id"] == course_id:
            return course

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


@app.put("/api/courses/{course_id}")
async def update_course(
        course_id: int,
        updated: schemas.CourseUpdate
):

    for course in courses:

        if course["id"] == course_id:

            data = updated.model_dump(exclude_unset=True)

            for key, value in data.items():
                course[key] = value

            return course

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


@app.delete("/api/courses/{course_id}")
async def delete_course(course_id: int):

    for course in courses:

        if course["id"] == course_id:
            courses.remove(course)
            return {"message": "Deleted"}

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )