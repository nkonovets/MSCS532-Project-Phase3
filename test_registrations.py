import unittest

from entities import Student, Course
from wait_list import Waitlist
from registration import student_registration, drop_course

import random


class TestRegistrationSystem(unittest.TestCase):

    def test_rules(self):          # every rule that can stop a registration

        course = Course("MSCS532", 200, 1, [("Mon", 9, 10)], {"ITSI336"})
        freshman = Student("S1", 1, set())
        sophomore = Student("S2", 2, {"ITSI336"})

        self.assertIn("level", student_registration(Student("S0", 1, set()), Course("BADM331", 400, 5, [("Tue", 9, 10)], set())))

        self.assertIn("prerequisites", student_registration(freshman, course))

        self.assertIn("registered", student_registration(sophomore, course))

        self.assertIn("already", student_registration(sophomore, course))

        self.assertEqual(student_registration(sophomore, Course("ITSS441", 100, 5, [("Mon", 9, 11)], set())), "Time conflict")

        self.assertEqual(student_registration(Student("S3", 2, {"ITSI336"}), course), "Added to waiting list")

    def test_waitlist_order(self):              # priority first, then registration order

        waitlist = Waitlist()

        for student_id, priority in [("A", 2), ("B", 4), ("C", 4), ("D", 1), ("E", 9)]:
            waitlist.addentry(student_id, priority)


        self.assertEqual([waitlist.get_first_student() for _ in range(5)], ["E", "B", "C", "A", "D"])


        with self.assertRaises(IndexError):     # empty waitlist
            waitlist.get_first_student()

    def test_drop_course(self):                 # the seat goes to the top of the waitlist
        
        course = Course("ITSI336", 100, 1, [("Mon", 9, 10)], set())
        owner, freshman, senior = Student("S1", 2, set()), Student("S2", 1, set()), Student("S3", 4, set())
        students = {s.id: s for s in (owner, freshman, senior)}

        for student in (owner, freshman, senior):
            student_registration(student, course)


        drop_course(owner, course, students)

        self.assertEqual(course.enrolled, {"S3"})


        self.assertIn("not registered", drop_course(owner, course, students))






    


def stress_test():                  #test how system holds against large number of students

    waitlist = Waitlist()

    for i in range(100_000):
        waitlist.addentry(f"S{i}", random.randint(1, 4))

    for i in random.sample(range(100_000), 20_000):
        waitlist.remove_student(f"S{i}")

    years = []

    while waitlist.is_empty() == False:                  #take every student out and save their year


        years.append(waitlist.heap[0].priority) 
        student_id = waitlist.get_first_student()

        print(len(years), student_id, years[-1])

    print("students left:", len(years))                                            
    print("higher years came out first:", years == sorted(years, reverse=True))



def edge_test():              #test unusual situations 

    waitlist = Waitlist()

    print("remove a student who is not there:", waitlist.remove_student("S1")) 
    waitlist.addentry("S1", 2)

    print("remove a student who is there:", waitlist.remove_student("S1"))  
           
    print("waitlist is empty after that:", waitlist.is_empty())       

    course = Course("ITSI336", 100, 0, [("Mon", 9, 10)], set())       

    print("course with 0 seats:", student_registration(Student("S2", 1, set()), course))   



def testnow():
    edge_test()
    stress_test()



if __name__ == "__main__":
    unittest.main()






