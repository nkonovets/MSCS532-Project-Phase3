import random

from entities import Student, Course

weekd = ["Mon", "Tue", "Wed", "Thu", "Fri"]


def make_courses(number_of_courses, rng):       # random courses with 1 or 2 meetings a week

    courses = {}

    for i in range(number_of_courses):          # loop to create every course


        course_id = f"C{i}"
        meetings = []

        for day in rng.sample(weekd, rng.randint(1, 2)):

            start = rng.randint(8, 17)
            meetings.append((day, start, start + rng.randint(1, 2)))


        courses[course_id] = Course(course_id, 100 * rng.randint(1, 4), rng.randint(20, 60), meetings, set())

    return courses


def make_students(number_of_students, rng):     # random students with a year from 1 to 4

    students = {}

    for i in range(number_of_students):         # loop to create every student

        student_id = f"S{i}"
        students[student_id] = Student(student_id, rng.randint(1, 4), set())

    return students


def make_data(number_of_students, number_of_courses, seed=42):     

    rng = random.Random(seed)

    courses = make_courses(number_of_courses, rng)
    students = make_students(number_of_students, rng)

    return students, courses