from entities import Student, Course
from registration import student_registration, drop_course

students = {                                    # students and courses are stored in dictionaries, so I can find them by id
    "S1": Student("S1", 1, set()),
    "S2": Student("S2", 2, {"ITSI336"}),
    "S3": Student("S3", 3, {"ITSI336"}),
    "S4": Student("S4", 4, {"ITSI336"}),
}
courses = {
    "ITSI336": Course("ITSI336", 100, 1, [("Mon", 9, 10)], set()),
    "MSCS532": Course("MSCS532", 200, 1, [("Tue", 9, 10)], {"ITSI336"}),
}


def register(student_id, course_id):            # register a student and print the result
    print(f"{student_id} -> {course_id}:", student_registration(students[student_id], courses[course_id]))


def demo_run():

    register("S1", "ITSI336")                     # gets the only seat
    register("S1", "ITSI336")                     # already registered
    register("S1", "MSCS532")                     # missing prerequisite
    register("S2", "MSCS532")                     # gets the only seat
    register("S3", "MSCS532")                     # course is full, goes to the waitlist
    register("S4", "MSCS532")                     # senior, goes ahead of S3

    print(drop_course(students["S2"], courses["MSCS532"], students))      # S4 will get the seat