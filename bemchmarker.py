import csv
import random
import time
import tracemalloc

from data_generator import make_data
from registration import student_registration
from wait_list import Waitlist


def run_benchmark(version):         # time registration and waitlist removal for 3 data sizes

    with open(f"results_{version}.csv", "w", newline="") as f:

        writer = csv.writer(f)
        writer.writerow(["n", "registration_ms", "waitlist_remove_ms", "memory_kb"])

        for n in [1_000, 10_000, 100_000]:     # loop through every data size

            rng = random.Random(1)              # same random choices every run

            tracemalloc.start()

            students, courses = make_data(n, n // 20)
            memory = tracemalloc.get_traced_memory()[1] / 1024

            tracemalloc.stop()

            course_ids = list(courses)

            start = time.perf_counter()

            for student in students.values():   # every student tries 5 random courses

                for course_id in rng.sample(course_ids, 5):
                    student_registration(student, courses[course_id])


            registration = (time.perf_counter() - start) * 1000

            waitlist = Waitlist()

            for student in students.values():   # all students wait for one course
                waitlist.addentry(student.id, student.year)

            start = time.perf_counter()

            for student_id in rng.sample(list(students), 500):     # 500 random students leave
                waitlist.remove_student(student_id)

            removal = (time.perf_counter() - start) * 1000

            row = [n, round(registration, 2), round(removal, 2), round(memory, 1)]

            
            writer.writerow(row)
            print(row)
