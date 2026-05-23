# class Simple:
#     college="sarathi"
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def show(self):
#         print(self.a,self.b)
#         print(Simple.college)
#     @classmethod
#     def show1(cls,name):
#         print(cls.college)
#         cls.name=name
#         print(cls.name)

#     @staticmethod
#     def show2():
#         k=10
#         print(k,"k")
#         print(Simple.college,"class variables")
# s=Simple(10,20)
# s.b=30
# s.show()
# s.show1()
# s.show2()
# s1=Simple(20,10)
# s1.show()
#Random number generaion
# import random
# r=random.randint(1,999999)
# print(r)
keys_list = ['A', 'B', 'C',"A"]
values_list = ['blue', 'red', 'bold',"s"]
d={}
for i,j in zip(keys_list,values_list):
    d[i]=j
print(d)
from collections import Counter
my_list = [8,4,8,2,2,5,8,0,3,5,2,5,8,9,3,8]
print(Counter(my_list))
d={}
# for i in my_list:
#     if my_list.count(i):
#         print(i)
# class Student:
#     a="MY FAMILY HIGH SCHOOL"
#     def __init__(self):
#         print(self.a,"constuctor execution")
#     def display1(self,*args):
#         print(*args)
#         print("ok")
#     @classmethod
#     def simple(cls):
#         print("classmethod")
#     @staticmethod
#     def display():
#         s=100
#         s1=200
#         print(s+s1,"addition")
#         print(Student.a)
# s=Student()
# print(s.a)
# s1=Student()
# print(s1.a)
# # s.show(2,10,20,20)
# print(Student.a)
# Student.a=100
# print(Student.a)
# Student.display()
# # Student.show(30)
# Student.simple()
# s.display()
# # s.show(30)
# s.simple()
# s.display1(11)
# Student.display1(11)
# s1.a="My"
# print(s1.a);print(s.a)
# nest=[[1,2],[4,[5],10],[8,9]]
# print([j for i in nest for j in i])
# d={1:2,3:4,5:6}
# d1={7:8,9:10}
# d.update(d1)
# print(d,"updae")
# d2={d,d1};print(d2)
class Student:
    school="My"
    def __init__(self,s,n):
        self.n=n
        self.s=s
    def show3(self):
        print("hello")
    @classmethod
    def show(cls):
        cls.school="My2"
        print("class mehod")
    @staticmethod
    def show1():
        print("satic execution")
# s=Student()
# s.show()
# Student.show(1)
# print
Student.show3(9)
Student.show()
Student.show1()
s=Student(10,12)
s.show1();s.show();s.show3()
s1=Student(1,2)
print(Student.school)
p=Student(2,3)
p.school="my10                                                                                                                                                                  "
print(p.school)

