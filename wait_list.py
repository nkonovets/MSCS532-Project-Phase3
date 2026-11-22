class WaitListStudent:

    __slots__ = ("student_id", "priority", "q_spot")

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
        self.position = {}          #changes in op1: student id 
        self.next_q_number = 0


    def is_empty(self):             #check if the waitlist is empty
        return len(self.heap) == 0

    def __contains__(self, student_id):     #check if the student is in the list by his id
        return student_id in self.position          

    def swap(self, i, j):           #swap two students and update where they are now
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.position[self.heap[i].student_id] = i
        self.position[self.heap[j].student_id] = j

    def sift_down(self, i):         #move the student down while a child is bigger

        while True:
            biggest = i

            for child in (2 * i + 1, 2 * i + 2):        #check both children

                if child < len(self.heap) and self.heap[child] > self.heap[biggest]:
                    biggest = child

            if biggest == i:
                break

            self.swap(i, biggest)
            i = biggest

        
    def sift_up(self, i):
        
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            self.swap(i, (i - 1) // 2)          
            i = (i - 1) // 2

    def addentry(self, student_id, priority):

        if student_id in self.position:         
            raise ValueError("This stydent is already in the waitlist")
        
        else:
            self.heap.append(WaitListStudent(student_id, priority, self.next_q_number))
            self.next_q_number += 1
            self.position[student_id] = len(self.heap) - 1      
            self.sift_up(len(self.heap) - 1)

    def get_first_student(self): # get the first student in the waitlist (the one with the highest priority)
         
        if self.is_empty():
            raise IndexError("waitlist is empty")
         
        self.swap(0, len(self.heap) - 1)        
        top_entry = self.heap.pop()
    
        del self.position[top_entry.student_id]         
        self.sift_down(0)                       
    
        return top_entry.student_id

    def remove_student(self, student_id):   #remove student from the waitlist with their ID


        if student_id not in self.position:     
            return False
        i = self.position[student_id]           #changed: find the student right away, no loop
        self.swap(i, len(self.heap) - 1)       

        self.heap.pop()
        del self.position[student_id]     

        if i < len(self.heap):          #the entry moved into this spot may need to go up or down
            self.sift_up(i)
            self.sift_down(i)     

        return True