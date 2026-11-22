# MSCS532 Project Phase 2: Student Course Registration System (Proof of Concept)

A partial implementation of the course registration system designed in Phase 1. It focuses on the core of the application: registering students for courses, checking the registration rules, and keeping a priority waitlist for full courses.

## How to run

```bash
python3 demo_run.py
```

Tests:

```bash
python3 -m unittest -v
```

## What is implemented

- Students and courses are stored in dictionaries (hash tables), so they can be found by ID.
- `student_registration()` checks, in order: already registered or waitlisted, course level for the student's year, prerequisites, time conflict, and free seats. If the course is full, the student goes to the waitlist.
- The waitlist is a binary heap, so adding a student and taking the next one both take O(log n) time. Priority is the student's year, and students with the same priority are served in the order they joined.
- `drop_course()` removes a student from a course or from its waitlist, and the first student on the waitlist takes the free seat.

## Not implemented yet

- The prerequisite graph with chains of prerequisites and cycle detection.
- Major requirements, graduation terms and advisor overrides.
- Testing with large data sets and many students at the same time.
