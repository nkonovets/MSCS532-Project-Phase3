from heap_sort import swap, siftDOwn

class WaitListStudent:

    def __init__(self, student_id, priority, q_spot): #student entity
        self.student_id = student_id
        self.priority = priority
        self.q_spot = q_spot

    def __gt__(self, other): #greater then function to use with python >
        
        if self.priority != other.priority:
            return self.priority > other.priority
        return self.q_spot < other.q_spot
    
    def __lt__(self, other): #less than (python <)
        return other > self

    def __ge__(self, other): #greater or equal (python >=)
        return not other > self

class Waitlist:

    def __init__(self,): #make awaitlist entity
        self.heap = []
        self.student_ids = set()
        self.next_q_number = 0


    def is_empty(self):             #check if the waitlist is empty
        return len(self.heap) == 0

    def __contains__(self, student_id):     #check if the student is in the list by his id
        return student_id in self.student_ids

        
    def sift_up(self, i):
        
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            swap(self.heap, i, (i - 1) // 2)
            i = (i - 1) // 2

    def addentry(self, student_id, priority):

        if student_id in self.student_ids:
            raise ValueError("This stydent is already in the waitlist")
        else:
            self.heap.append(WaitListStudent(student_id, priority, self.next_q_number))
            self.next_q_number += 1
            self.student_ids.add(student_id)
            self.sift_up(len(self.heap) - 1)

    def get_first_student(self): # get the first student in the waitlist (the one with the highest priority)
         
        if self.is_empty():
            raise IndexError("waitlist is empty")
         
        swap(self.heap, 0, len(self.heap) - 1)
        top_entry = self.heap.pop()
    
        self.student_ids.remove(top_entry.student_id)
        siftDOwn(self.heap, 0, len(self.heap))
    
        return top_entry.student_id

    def remove_student(self, student_id):   #remove student from the waitlist with their ID
        if student_id not in self.student_ids:
            return False
        for i in range(len(self.heap)): # loop to find the student in the heap
            if self.heap[i].student_id == student_id:
                break
        swap(self.heap, i, len(self.heap) - 1)
        self.heap.pop()
        self.student_ids.remove(student_id)
        if i < len(self.heap):          # the entry moved into this spot may need to go up or down
            self.sift_up(i)
            siftDOwn(self.heap, i, len(self.heap))
        return True


    


