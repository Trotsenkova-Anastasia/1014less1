
print("Hello")

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
#
#
# import random
# class Student:
#     def __init__(self, name):  #створюємо студента
#         self.name = name
#         self.gladness = 50
#         self.progress = 0
#         self.alive = True
#
#     def to_study(self): #студент навчається
#         print("Time to study")
#         self.progress += 0.12
#         self.gladness -= 5
#
#     def to_sleep(self): #спить
#         print("I will sleep")
#         self.gladness += 3
#
#     def to_chill(self): #відпочиває
#         print("Rest time")
#         self.gladness += 5
#         self.progress -= 0.1
#
#     def is_alive(self): #статистика, слідкуюи за його характеристиками
#         if self.progress < -0.5:
#             print("Cast out…")
#             self.alive = False
#         elif self.gladness <= 0:
#             print("Depression…")
#             self.alive = False
#         elif self.progress > 5:
#             print("Passed externally…")
#             self.alive = False
#
#     def end_of_day(self): # кінець дня
#         print(f"Gladness = {self.gladness}")
#         print(f"Progress = {round(self.progress, 2)}")
#
#     def live(self, day): # генерація дня студента
#         day = "Day" + str(day) + "of" +self.name + "life"
#         print(f"{day:=^50}")
#         live_cube = random.randint(1, 3)
#         if live_cube == 1:
#             self.to_study()
#         elif live_cube == 2:
#             self.to_sleep()
#         elif live_cube == 3:
#             self.to_chill()
#         self.end_of_day()
#         self.is_alive()
#
# nick = Student(name="Nick")
# for day in range(365): #проходимось по всім дням у році
#     if nick.alive == False:
#         break
#     nick.live(day)



#
# class Human:
#     def __init__(self, name="Human"):
#         self.name = name
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#     # def add_passenger(self, human):
#     #     self.passengers.append(human)
#     def add_passenger(self, *args):
#         for passenger in args:
#             self.passengers.append(passenger)
#     def print_passengers_names(self):
#         if self.passengers!= []:
#             print(f"Names of {self.brand} passengers:")
#             for passenger in self.passengers:
#                 print(passenger.name)
#         else:
#             print(f"There are no passengersin {self.brand}")
#
# nick = Human("Nick")
# kate = Human("Kate")
# car = Auto("Mercedes")
#
# car.add_passenger(nick)
# car.add_passenger(kate)
# car.print_passengers_names()
#
#
#
# class Human:
#     height = 170
#     sat=50
# class Student(Human):
#     sat = 100
# class Worker(Human):
#     sat = 150
#
# nick = Student()
# ann = Worker()
# print(nick.height)
# print(ann.height)
#
# print(nick.sat)
# print(ann.sat)
#
# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60
# class Parent(Grandparent):
#     age = 40
#
# class Child(Parent):
#     height = 50
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)
# print()
# nick = Child()
#
#
# print()

# class Hello_world:
#     hello = "Hello"
#     _hello = "_Hello"
#     __hello = "__Hello"
#     def __init__(self):
#         self.world = "World"
#         self._world = "_World"
#         self.__world = "__World"
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
#         print()
# class Hi(Hello_world):
#     def hi_print(self):
#         print(self.hello)
#         print(self.world)
#         print(self._hello)
#         print(self._world)
#         print(self.__hello)
#         print(self.__world)
#
# hello = Hello_world()
# hello.printer()
# hi = Hi()
# hi.hi_print()

#
# class Computer:
#     def calculate(self):
#         print("Calculating…")
#
#     def __init__(self):
#         super().__init__()
#         self.memory = 128
# class Display:
#     def display(self):
#         print("I display the image on the screen…")
#
#     def __init__(self):
#         super().__init__()
#         self.resolution = "4k"
#
# class SmartPhone(Display, Computer):
#     def print_info(self):
#         print(self.resolution)
#         print(self.memory)
# iphone = SmartPhone()
# iphone.calculate()
# iphone.display()
#
# iphone.print_info()