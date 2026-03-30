import json
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

cursor.execute("DELETE FROM Meetings")
cursor.execute("DELETE FROM Courses")

with open("fal26.json") as f:
    data = json.load(f)

seen = set()
for course in data:
    if course["crn"] not in seen:

        enrollment = course.get("enrollment", {})
        course_values = (
            course["crn"],
            course["course_code"],
            course["department"],
            course["course_title"],
            course["grad_requirements"],
            course["enrollment"]["current"],
            course["enrollment"]["max"],
            course["enrollment"]["remaining"]
        )

        cursor.execute("""
            INSERT INTO Courses
            (crn, course_code, department, course_title, grad_requirements,
            enroll_current, enroll_max, enroll_remaining)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, course_values)
        seen.add(course["crn"])

    for meeting in course["meetings"]:
        meeting_values = (
            course["crn"],
            meeting["meeting_type"],
            meeting["weekdays"],
            meeting["start_time"],
            meeting["end_time"],
            meeting["class_time"],
            meeting["room"]
        )

        cursor.execute("""
            INSERT INTO Meetings
            (crn, meeting_type, weekdays, start_time, end_time, class_time, room)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, meeting_values)

conn.commit()
cursor.close()
conn.close()

print("Database successfully populated.")