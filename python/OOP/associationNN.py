class Student:
    def __init__(self, name: str):
        self.name: str = name
        self.courses: list['Course'] = [] # list of Course objects

    def take_course(self, course: 'Course'):
        self.courses.append(course) # reference from Student to Course

class Course:
    def __init__(self, name: str):
        self.name: str = name

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
