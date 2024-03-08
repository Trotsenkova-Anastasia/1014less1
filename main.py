# class Student:
#     name="Alex"
#     def __init__(self):
#         self.name="Nick"
#         self.age=12
#         print(self.age)
#
#
# student1=Student()
# Student.__init__(self=student1)
#
#
# print(student1.name)
# class Student:
#     def __init__(self):
#         self.height = 170
#
#     height = 160
#
#     def printer(self):
#         print(self.height)
#
# nick = Student()
# nick.printer()


import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

nick = Student("Alex")
