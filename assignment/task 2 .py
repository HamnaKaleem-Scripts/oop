class Person:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact
    def __str__(self):
        return f"Name: {self.name}, Contact Number: {self.contact}"
class Student(Person):
    def __init__(self,name,contact,dep,sem):
        super().__init__(name,contact)
        self.dep=dep
        self.sem=sem
    def __str__(self):
        return f"Name: {self.name}, Contact Number: {self.contact}, Department: {self.dep}, Semester: {self.sem}"
class Teacher(Person):  
    def __init__(self,name,contact,course,off_num):
        Person.__init__(name,contact)
        self.course=course  
        self.off_num=off_num
    def __str__(self):
        return f"Name: {self.name}, Contact Number: {self.contact},Course: {self.course}, Office Number: {self.off_num}"
class TA (Teacher,Student):
    def __init__(self, name, contact, course, sem, dep, off_num):
        Teacher.__init__(self, name, contact, course, off_num)
        Student.__init__(self, name, contact, dep, sem)
        
        # super().__init__(name, contact, dep, sem)
        # super().__init__(course, off_num)
        # super(Student, self).__init__(name, contact, dep, sem)
        # super(Teacher, self).__init__(name, contact, course, off_num)
    def __str__(self):
           return f"Name: {self.name}, Contact Number: {self.contact}, Department: {self.dep}, Semester: {self.sem},Course: , Office Number: "

def main():
    person = Person("John Doe", "123-456-7890")
    print(person)
    print()

    student = Student("Alice ", "987-654-3210", "Computer Science", 3)
    print(student)
    print()

    teacher = Teacher("Johnson", "555-123-4567", "Computer Science", 301)
    print(teacher)
    print()

    ta = TA("Bob ", "777-888-9999", "Physics", 2, "Quantum Mechanics", 102)
    # ta=TA()
    print(ta)
main() 