# MSCS532 Project Phase 3: Student Course Registration System (Optimization and Scaling)

The Phase 2 registration system, optimized and tested with large data sets (1,000, 10,000 and 100,000 students).

## How to run

```bash
python3 main.py
```

Tests:

Choose `d` for the demo, `b` for the benchmark, or `t` for the edge and stress tests.

## What is implemented

- Students and courses are stored in dictionaries (hash tables), so they can be found by ID.
- `student_registration()` checks, in order: already registered or waitlisted, course level for the student's year, prerequisites, time conflict, and free seats. If the course is full, the student goes to the waitlist.
- The waitlist is a binary heap, so adding a student and taking the next one both take O(log n) time. Priority is the student's year, and students with the same priority are served in the order they joined.
- `drop_course()` removes a student from a course or from its waitlist, and the first student on the waitlist takes the free seat.
- optimization 1: the waitlist keeps a dictionary of each student's position in the heap, so removing a student no longer searches the whole list (removing 500 students from 100,000 went from about 824 ms to 1.4 ms).
optimization 2: `__slots__` in the classes, about 10% less memory.

## Not implemented yet

- The prerequisite graph with chains of prerequisites and cycle detection.
- Major requirements, graduation terms and advisor overrides.

