import unittest

from entities import Student, Course
from wait_list import Waitlist
from registration import student_registration, drop_course


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


if __name__ == "__main__":
    unittest.main()