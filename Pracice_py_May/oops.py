# my_list = [8,4,8,2,2,5,8,0,3,5,2,5,8,9,3,8]
# d={}
# print(max(my_list))
# for i in my_list:
#     if i  in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)
# l1=[]

# for k,v in d.items():
#     l1.append(v)
# l2=l1[0]
# for i in l1:
#     if i>l2:
#         l2=i
# print(l2)
# for k,v in d.items():
#     if v in l1:
#         print(f"{k}:{v}")s
from collections import Counter
# s="puvvada bala venkata ramanjaneyulu"
# l=[1,2,3,4,5,8,9]
# my_list = [8,4,8,2,2,5,8,0,3,5,2,5,8,9,3,8]
# d={"a":10}
# e=1,2,4,5,9,9
# print(Counter(s));print(Counter(l));print(Counter(d));print(Counter(e))
# print(Counter(my_list).most_common(1))
###############################################################OOOPS############################
# class Test:
#     def __init__(self):
#         pass
#     def m1(self):
#         return "Balaji"
#     def m2(self):
#         return "omkar"
#     # def __str__(self):
#     #     return f" Bangaram"
#     def __repr__(self):
#         return f" love you Bangaram"
# t=Test()
# t1=Test()
# # # t.m1()
# # # t.m2()
# print(t);print(t1)
#####################################
#__str__ and __repr__
# import datetime
# dt=datetime.datetime.now()
# s1=str(dt)
# print(s1,"String epresenation")
# # e=eval(s1)
# # print(e)
# ###########now repr using#################3333333
# r=repr(dt);print(r)
# r1=eval(r);print(r1)
#####################################################
# from abc import ABC,abstractmethod
# class Student(ABC):
#     @abstractmethod   
#     def display(self):
#         pass
#     def simple(Self):
#         return "Infosys"
# class Teacher(Student):
#     def display(self):
#         pass
#     def __str__(self):
#         return f"HI anna"

# s=Teacher();print(s)#;print(s.display());print(s.simple())
##############################################################################
#Access Specifiers
# class MyFamily:
#     def __init__(self,name,age,mobile):
#         self.__age=age
#         self.name=name
#         self._mobile=mobile
#     def display(self):
#         return f"{self.name},{self.__age},{self._mobile}"
# class MyFamily1(MyFamily):
#         # def __init__(self,name,age,mobile):
#         #     super().__init__(name,age,mobile)
#         def display(self):
#             return super().display()
#             print("ok")
# # m=MyFamily("Home",30,8008887078)
# # print(m);
# # print(m.display())
# # print(m.name);print(m._mobile);print(m._MyFamily__age);
# m=MyFamily1("Home1",30,8008887078)
# print(m.display())
# print(m.display())
# print(m.name);print(m._mobile);print(m._MyFamily__age);
####################################################Polymorphism###############################
#Compile time overloading---method and consructor
# class Person:
#     def __init__(self,a=None,name=None):
#         self.a=a
#     def __init__(self,a,name):
#         self.name=name
#         self.a=a
#     def simple(self):
#         print("constructor overloading")
#         print(self.name);print(self.a)
# #p=Person("samanha")
# p1=Person("Shyam",10)
# p1.simple()#;p.simple()
class Person1:
    def __init__(self,*n):
       print("hi dude")

    
p=Person1(1);p1=Person1(1,2);p3=Person1(1,2,3,4,56,67,78)
print(p);print(p1);print(p3)
# p.simple();p1.simple();p3.simple()
# class MethodOveload:
#     def simple(self,a=None):
#         print("hi")
#     def simple(self,a,b):
#         print("seccond Hello")
#     def simple(self,a,b,c):
#         print("3d Hello")
#     def simple(self,*args):
#         print("smkdlm")
# m=MethodOveload()
# m.simple(1,24,5,6,7,8,8)
#method overriding
# class Teacher:
#     def simple(self):
#         print("Hello Megastar")
# class Student(Teacher):
#     def simple(self):
#         # super().simple()
#         print("Katrinkif")
# s=Student()
# s.simple()
#############################################
#Diamond Problem MRO Algorithem 
class A:
    def simple(self):
        print("Hi from A")
class B:
    def simple(self):
        print("Hi from B")
class C(B):
    def simple(self):
        print("Hi from C")
class D(B):
    def simple(self):
        print("Hi form D")
class E(A,D,C):
    def simple(self):
        print("Hi from E")
e=E()
e.simple()
print(E.__mro__)

class Balaji:
    def __init__(self,name):
        self.name=name
        print("HI Welcome to my familyh")
    def __str__(self):
        return f"Hi {self.name}"
b=Balaji("Balau727")
print(b)
c=Balaji("VENKI");print(c)



































































