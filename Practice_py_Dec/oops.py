# class Student:
#     school="MyFamilyHouse"
#     def __init__(self):
#         self.a=10
#         self.b=11
#     def simple(self):
#         print(self.school)
#         return f"Hello addition  {self.a+self.b}"
# s=Student()
# print(s.simple())
# class Student:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __mul__(self,others):
#         return Student(self.a*others.a,self.b*others.b)
# s1=Student(10,20)
# s2=Student(2,3)
# s3=Student(3,2)
# s4=s1*s2*s3
# print(s4.a,s4.b)
# def str2(v):
#     if v>0:
#         raise ValueError("Arithmeic error")
#     return v
# # print(str2(-10))
# print(str2(10))

# class singleton:
#     _instance=None
#     def __new__(cls,*a,**kw):
#         if not cls._instance:
#            cls._instance=super(singleton,cls).__new__(cls,*a,**kw)
#         return f"already created"
# Single=singleton()
# Single3=singleton()
# print(Single is Single3)
#You are developing a simple library management system, and you need to represent books and their information,
#  such as title, author, and ISBN. Each book should be treated as an object, and you should be able to create multiple book objects with unique information. Describe how you would set up a Book class in Python. 
# class Book:
#     def __init__(self,title,author,isbn):
#         self.title=title
#         self.author=author
#         self.isbn=isbn
#     def simple(self):
#         return  f"{self.title},{self.author},{self.isbn}"
# o=Book("Python","Ram",900)
# print(o.simple())
# class VideoGame:
#     health=100
#     def __init__(self,name,level):
#         self.name=name
#         self.level=level
#     def simple(self):
#         print(self.name,self.level,VideoGame.health)
# v=VideoGame("BALA",2)
# v1=VideoGame("Rama",3)
# v.simple()
# v1.simple()
# class Employee:
#     def __init__(self,name,salry):
#         self.name=name
#         self.salary=salry
# class Manager(Employee):
#     def __init__(self,name,salary,department):
#         super().__init__(name,salary)
#         self.department=department
# m=Manager("balaji",2000,"it")
# print(m.name)
# print(m.salary)
# print(m.department)
# class BasicAccount:
#     def __init__(self,balance):
#         self._balance=balance
#     def simple(self):
#         return self._balance
# class SavingsAccount(BasicAccount):
#     def __init__(self,balance,interset):
#         super().__init__(balance)
#         self.interset=interset
#     def simple(self):
#         return self._balance*self.interset
# b=BasicAccount(1000)
# print(b.simple())
# s=SavingsAccount(1000,0.05)
# print(s.simple())
# class Shop:
#     vis=0
#     def __init__(self,person):
#         self.person=person
#         Shop.vis+=1
# s=Shop("Balaji")
# s1=Shop("Ramu")
# s3=Shop("Arish")
# print(Shop.vis)
# from abc import ABC,abstractmethod
# class Student(ABC):
#     @abstractmethod
#     def simple(self):
#         pass
# class Teacher(Student):
#     def simple(self):
#         return True
# class Employee(Student):
#     def simple(self):
#         return False
# t=Teacher()
# print(t.simple())
# t=Employee()
# print(t.simple())

# print(2**3)
print(0**0)

# class Student:
#     id={101,105}
#     def __init__(self,name,exid):
#         if exid not in Student.id:
#             raise ValueError("already id is allocated")
#         self.name=name
#         self.exid=exid
#         Student.id.add(exid)
# s=Student("bala",103)
# s1=Student("Bala1",102)

# class Myhome:
#     def __init__(self,register):
#         self.register=register
#     def __eq__(self,others):
#         print("hello")
#         return self.register==others.register
# m=Myhome("AP09GZ0345")
# m1=Myhome("AP08GZ0345")
# print(m==m1)
# print(m1==m)
# class MyHome:
#     def __init__(self,qid,question,qans):
#         self.qid=qid
#         self.question=question
#         self.qans=qans
#     def simple(self,ans):
#         print(self.qid,self.question,self.qans)
#         return ans==self.qans
# m=MyHome(101,"wha is india capital","Delhi")
# print(m.simple("Delhi"))
# class Pyht:
#     def __init__(self,sname):
#         self.sname=sname
#         self.course1=[]
#         self.dic={}
#     def simple(self,course):
     
#         self.course1.append(course)
#         print(self.course1)
#         self.dic[self.sname]=self.course1.append(course)
#         return self.dic
# p=Pyht("balaji")
# p.simple("Pyhotn")
# p.simple("SQL")
# p1=Pyht("OMkar")
# p1.simple("Arithematic")
# print(p.course1)
# print(p.dic)

# class PlayStation:
#     def __init__(self,name):
#         self.name=name
#         self.Playlist={}
#     def sample(self,playname):
#         self.Playlist[playname]=[]
#     def play(self,listof):
#         if
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def simple(self,others):
#         if self.salary>=others.salary:
#             print("Higher salary")
#         else:
#             print("Lower salary")
# e=Employee("Balaji",2000)
# e1=Employee("Arish",2000)
# e.simple(e1)
#In a financial application, you have different types of accounts: savings and checking. 
# Each type of account has different rules for withdrawals. 
# Savings accounts allow limited withdrawals, while checking accounts allow unlimited withdrawals but may charge a fee. You need to design a flexible structure to handle these variations. 
# class BA:
#     def __init__(self,a,b=0,c=0):
#         self.a=a
#         self.b=b
#         self.c=c
# class Savings(BA):
#     def deposit(self,amount):
#         self.b+=amount
#     def withdraw(self,amount):
#         if  self.b>=amount and self.c<2:
#             print("Transcation completed")
#             self.b=self.b-amount
#             self.c+=1
#             print(self.c)
#             print(self.b)
        
# s=Savings(101)
# s.deposit(1000)
# print(s.b)
# s.deposit(5000)
# print(s.b)
# s.withdraw(500)
# s.withdraw(500)
# s.withdraw(700)

# class EDevices:
#     def __init__(self):
#         self.a=10
#     def execute(self):
#         return f"Hello"
# class Lights(EDevices):
#     def execute(self,command):
#         return "lights on" if command=="on" else "lights off {self.a}"
# class Camera(EDevices):
#     def execute(self,command):
#         return "record starr" if command=="ON" else "Not recording"


# l=Lights()
# print(l.execute("off"))

# CA=Camera()
# print(CA.execute("ON"))
# class HMS:
#     def __init__(self,category):
#         self.category=category
#     def responsibitiy(self):
#         return f"{self.category}"
# class Doctor(HMS):
#     def __init__(self,category):
#         super().__init__(category)
#     def responsibitiy(self,type1):
        
#         if type1=="Doctor":
#             print("The timings between 6 to 9")
#         elif type1=="Nurse":
#             print("he ony day time")
#         return super().responsibitiy()
        

# d=Doctor("Hospital")   
# print(d.responsibitiy("Docto"))   
# import math
# class Shape:
#     def __init__(self,radius=5,length=4,):
#         self.radius=5
#         self.length=4
#         self.base = 3
#         self.height = 6
#     def calc(self):
#         return f"perform each class calculation "
#     def circle(self):
#         return math.pi *self.radius**2
#     def square(self):
#         return self.length**2
#     def triangle(self):
#         return 0.5*self.base*self.height
# s=Shape()
# print(s.calc())
# print(s.circle())
# print(s.square())
# print(s.triangle())
class Time:
    def nexts(self,)











        





