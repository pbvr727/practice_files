# print("selecct one option:")
# print("1.Addition")
# print("2.substraction")
# print("3.multipilation")
# choice=int(input("enter require number"))
# a=int(input("Enter a value:"))
# b=int(input("Enter b value:"))
# c=int(input("enter c value:"))
# if choice==1:
#     print("addition",a+b+c)
# elif choice==2:
#     print("substraction:",a-b-c)
# elif choice==3:
#     print("mul",a*b*c)
# else:
#     print("not peform anythong")
# for i in range(10):
#     print("hello\tvalue\t",i)
# l="Puvvada Anasurya"
# print(l[-3:-9:-1]*3)
# import datetime
# d1=datetime.datetime.now()
# print(d1)
# l=[5,2,3,9,7,1,12]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
l=[5,2,3,9,7,1,12]
# l1=[]
# target=12
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==target:
#             l1.append((l[i],l[j]))
# print(l1)
# k=[i for i in range(len(l)) if i%2!=0]
# print(k)
# y=lambda s:s**8
# print(y(2))
# import copy
# l=[5,2,3,[9,7],1,12]
# l1=copy.deepcopy(l)
# l[3][0]=10
# print(l1)
# print(l)
# l9=[5,2,3,9,16,1,12,8]
# p=list(map(lambda s:s*2,l9))
# print(p)
# p1=list(filter(lambda s:s%2==0,l9))
# print(p1)
# def recur():
#     l2=[]
#     for i in range(len(l)):
#         if isinstance(l[i],list):
#             l2.extend(l[i])
#         else:
#             l2.append(l[i])
#     return l2
# l=[5,2,3,[9,7],1,12]
# print(recur())
# import sys
# print(sys.getsizeof(a:=10))
# p="balaji"
# for i in range(len(p)):
#     print(p[i],"index=",i,end="\n")
from abc import *
class Student(ABC):
    @abstractmethod
    def show(self):
        pass
class Teacher(Student):
    def show(self):
        print("Hello How are you")
t=Teacher()
t.show()
class Student:
    def __init__(self,a,b):
        self.r=a
        self.o=b
    def show(self):
        return f"self.r+self.o"
s=Student(10,10)
s.show()

def decor1(func):
    def inner(*a,**k):
        t=0
        for i in a:
            t=t+i
            print(t)
        for k,v in k.items():
            print(k,v)
    return inner



@decor1
def add(a,b):
    print("How are you")
    c=a+b
    return f"{c}"
print(add(5,10,p=10,p1=89))


l1=[4,9,3,2,1,5,6,10]
for i in range(len(l1)):
    for j in range(i,len(l1)):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
print(l1)

l2=list(map(lambda d:d*5,l1))
print(l2)
l=[i for i in l1 if i%2==0]
print(l)
d={"a":100,'b':200,"c":300}
p="Puvvada Bala Venkata Ramanjaneyulu"
d={}
for i in p:
    if i in d:
        d[i]=1+d[i]
    else:
        d[i]=1
print(d) 
for j,k in d.items():
     










