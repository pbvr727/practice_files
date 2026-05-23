# ############oops##################
# class Emplyoee:
#     company="Helieus"
#     def __init__(self,eid):
#         self.eid=eid
#     def simple(self):
#         print(self.eid,Emplyoee.company)
#     @classmethod
#     def sample(cls,name):
#         cls.name=name
#         print(cls.name)
        
#     @staticmethod
#     def general():
#         print("Hello")
# e=Emplyoee(101)
# e.simple()
# e.sample("Balaji")
l=[2,4,21,89]
print(list(map(lambda x:x*2,l)))
print(list(filter(lambda x:x%2==0,l)))
from functools import reduce
print(reduce(lambda x,y:x*y,l))

def simple(*args,**kwar):
    for i in args:
        print(i)
    for k,v in kwar.items():
        print(k,":",v)
print(simple(10,23,45,90,0,c="Balajia",a="Arepalli"))
def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
l.sort()
print(l)
###############decoaror###################
# def decor(func):
#     def inner(*ar,**kw):
#         print("Hi")
#         result=func(*ar,**kw)
#         return result
#     return inner

# @decor
# def add(a,b):
#     return a+b
# print(add(5,6))

# import datetime

# def decor(func):
#     def inner(*ar,**kw):
#         st=datetime.datetime.now()
#         result=func(*ar,**kw)
#         end=datetime.datetime.now()
#         total=end-st
#         return result,total
#     return inner

# @decor
def simple(n):        
    l1=[]
    for i in range(2,n):
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            l1.append(i)
    return l1
print(simple(100))
# import json
# sudent={"Balaji":100,"age":20,"phone":9000}
# with open("info.txt","w") as f1:
#     json.dump(sudent,f1)
# with open("info.txt","r") as f2:
#     s=json.load(f2)
#     print(s)
# l=[1,2,34,5,]
# o=iter(l)
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))
# # print(next(o))
# def gen(n):
#     for i in range(n):
#         yield i
# g=gen(10)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# # print(g.__next__())
# # print(g.__next__())
# class Teacher:
#     _instance=None
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance=super().__new__(cls)
#         return cls._instance
# t1=Teacher()
# t2=Teacher()
# print(t1 is t2)



