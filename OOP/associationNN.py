class Student:
    def __init__(self, name):
        self.name = name
        self.courses = [] # list of Course objects

    def take_course(self, course):
        self.courses.append(course) # reference from Student to Course
        course.students.append(self) # reference from Course to Student

class Course:
    def __init__(self, name):
        self.name = name
        self.students = [] # list of Student objects
        # Note that the back-reference to Student is optional
        # and can be useful in some scenarios.

# Example of usage
student1 = Student("Alice")
student2 = Student("Bob")

course1 = Course("Math")
course2 = Course("Science")

student1.take_course(course1)
student1.take_course(course2)

student2.take_course(course1)

print(student1.name, "takes courses:", [course.name for course in student1.courses])
print(student2.name, "takes courses:", [course.name for course in student2.courses])

print(course1.name, "has students:", [student.name for student in course1.students])