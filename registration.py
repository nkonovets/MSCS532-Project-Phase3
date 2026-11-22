

def has_conflict(student, course):      # check if the meeting times has any conflict
    for registered_course in student.schedule:                                      
        for day, start, end in registered_course.meeting_times:
            for new_day, new_start, new_end in course.meeting_times:
                if day == new_day and start < new_end and new_start < end:          # if same day and the hours overlap
                    return True
    return False


def priority(student, course):          # students in a later year get a higher priority on the waitlist
    return student.year


def student_registration(student, course):      # registration funtcion

    if student.id in course.enrolled or student.id in course.waitlist:      # check for enrollment
        return "This student is already registered or waitlisted"

    if course.level // 100 > student.year + 1:      # checks if the course level suits the student's year
        return "Student cannot be registered for this course, the level of the course is too high for this student"

    if not course.prereqs <= student.completed_courses:     # check if the student has taken all the prerequisites
        return "Student cannot be registered for this course, student is missing prerequisites"

    if has_conflict(student, course):       # checks for course conflicts in meeting time
        return "Time conflict"

    if len(course.enrolled) < course.capacity:      # check if the course has seats available
        course.enrolled.add(student.id)
        student.schedule.append(course)

        return f"Student is registered for the course (ID:{course.id})"

    course.waitlist.addentry(student.id, priority(student, course))      
    return "Added to waiting list"


def drop_course(student, course, students):     
    if student.id in course.enrolled:

        course.enrolled.remove(student.id)
        student.schedule.remove(course)

        if not course.waitlist.is_empty():

            next_student = students[course.waitlist.get_first_student()]    # students is a dictionary: id - Student
            course.enrolled.add(next_student.id)

            next_student.schedule.append(course)

            return f"Student dropped the course, {next_student.id} moved from the waitlist into the course"

        
        return "Student dropped the course"

    if course.waitlist.remove_student(student.id):

        return "Student removed from the waitlist"

    return "This student is not registered for this course"