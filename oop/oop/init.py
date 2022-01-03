
class Teacher:
    def __init__(self, name, salary): # first parameter always = self
        self.name = name # self.name  = Second Parameter
        self.salary = salary # self.salary  = Third Parameter

teacherobj1 = Teacher("Mohon Lal Chy", 70000)
teacherobj2 = Teacher("Mohona Chaterjee", 50000)

print(teacherobj1.name)
print(teacherobj1.salary)

print(teacherobj2.name)
print(teacherobj2.salary)