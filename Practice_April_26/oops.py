# class Student:
#     school_name="RBPS"
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def simple(self):
#         print(self.a+self.b)
#     @classmethod
#     def simple1(cls,ss):
#         cls.ss=ss
#         print(cls.ss)
#     @staticmethod
#     def simple2():
#         y=10
#         z=20
#         print(y+z)
#         Student.phone=800
#         print(Student.phone)
# s=Student(10,40)
# Student.simple1(100)
# s.simple()
# s.simple2()
# class Person:
#     village_name="Kaza"
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#         print(self.a,self.b,self.c)
#     def simple(self):
#         print(self.a,self.b,self.c)
# class Teacher(Person):
#     name_of_teacher="Reshma"
#     village_name="Kaza1"
#     def __init__(self,a,b,c,emp):
#         super().__init__(a,b,c)
#         self.emp=emp
#         print(self.emp)
#     def simple2(self):
#         super().simple()
#         print("Hello Teacher")
# t=Teacher(10,20,30,"Balaji")
# t.simple2()
# print(super().village_name)
import datetime
def decor(func):
    def inner(*a,**k):
        start=datetime.datetime.now()
        t=0
        for i in a:
            t=t+i
        print(t)
        end=datetime.datetime.now()
        print(end-start)
        return func(a[0],a[1],a[2],a[3])
    
    return inner


@decor
def simple(*a,**b):
    print("a+b")
simple(2,8,16,23,balu=100)

def gen(n):
    for i in range(1,n):
        yield i
g=gen(10)
print(g.__next__())
print(g.__next__())
print(g.__next__())
l=[1,2,3,4,5]
l1=iter(l)
# for i in l1:
#     print(i)
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
x=151
temp=x
r=0
while 0<temp:
    d=temp%10
    r=r*10+d
    temp=temp//10
print(r)
if x==r:
    print("Palindrome")
else:
    print("Not Palindrome")
s="god"
s1="dog"
# s1=s[0]
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         if s[i]>s[j]:
#             s[j],s[i]=s[i],s[j]
# print(s)
# s2=sorted(s)
# s3=sorted(s1)
# print(s2,s3)
# if s2==s3:
#     print("annagram")
# else:
#     print("Not Anagram")
# s="bala venkata ramanjaneyulu"
# s1=list(s)
# for i in range(len(s1)):
#     for j in range(i+1,len(s1)):
#         if s1[i]>s1[j]:
#             s1[i],s1[j]=s1[j],s1[i]
# print("".join(s1))
# # print(s1)
# l=[3,10,9,6,4,5,2,1]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
# s="Ramanjaneyulu"
# print(s[::3])#0,3,6,9,12,15
# for i in range(0,len(s),3):
#     print(s[i])#Raayu
# p=""
# for i in range(len(s)):
#     p=s[i]+p
# print(p)
# print(1//10)
# r="If current index is beyond reachable range, you are stuck".split()
# for i in range(len(r)):
#     if i%2==0:
#         print(r[i][::-1])
# l=[1,2,3,4]
# a=l.copy()
# a.pop()
# print(l)
with open("hello.txt","w") as file1:
    file1.write("Hello\n")
    file1.write("I am Balaji")
import json
student={"name":"balji","Age":30,"phone":800888,"maried":False}
with open("file1.json","w") as f1:
    json.dump(student,f1)
with open("file1.json") as f:
    d=f.read()
    print(d)








    



