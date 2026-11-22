from wait_list import Waitlist

class Student:          

    def __init__(self, student_id, study_year, completed_courses):  #create a student entity with parameters
        self.id = student_id
        self.year = study_year  #year in school (e.g sophomore, junior, senior)
        self.completed_courses = completed_courses

        self.schedule = []  #current classes the student is registered for 


class Course:

    def __init__(self, course_id, level, seats, meeting_times, prereqs):
        
        self.id = course_id

        self.level = level      

        self.capacity = seats                        
        self.meeting_times = meeting_times  # list of (day, start hour, end hour), for example ("Mon", 9, 10)            
        self.prereqs = prereqs        

        self.enrolled = set()                           
        self.waitlist = Waitlist()                      
        