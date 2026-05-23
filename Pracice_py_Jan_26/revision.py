# def fun(n):
#     print("Hello"*n)
# fun(10)
# In a task scheduling application, tasks can have varying time intervals, such as daily, weekly, or monthly. 
# Each interval determines when the task should be scheduled next. 
# import datetime
# class TaskApp:
#     def specifytime(self):
#         print("Hello")
# class Day(TaskApp):
#     def specifytime(self):
#         return datetime.datetime.now()-datetime.timedelta(weeks=1)
# d=Day()
# print(d.specifytime())
# # print(dir(datetime))
# #Here we can use datetime.timedelta days and weeks to calculate intervals
# import turtle
# # print(dir(turtle))
# sq=turtle.Turtle()
# for i in range(4):
#     sq.forward(100)
#     sq.right(900)
#     sq.color("red")
# turtle.done()
# for i in range(4,0,-1):
#     for j in range(i):
#         print("7",end=" ")
#     for k in range(i-1):
#         print(k,end="")
#     print()
# for i in range(1,7):
#     for j in range(1,6-i):
#         print(" ",end=" ")
#     for k in range(6,6-i,-1):
#         print(k,end=" ")

#     print()
# for i in range(1,10):
#     print(i,i,i,end=" ")
#     print()
# for i in range(len("Puvvada Bala Venkata Ramanjaneyulu")):
#     print(i)
# a=20
# b=89
# def add():
#     a=10
#     print(a)
#     print(globals()['a']['b'])
#     print(add.__code__.co_nlocals)
# add()
# def sub():
#     a=35
#     print(a)
# sub()
s="Puvvada Bala Venkata Ramanjaneyulu".lower()
s1=sorted(s)
print(s1)
s2="".join(s1)
s3=set(s2)
print(s3)

# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         result=n*fact(n-1)
#         return result
# print(fact(5))
l=[1,3,2,4,8,4,9]
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
target=8
l1=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==target:
            l1.append((l[i],l[j]))
print(l1)

d={"a":[10],"b":10,"c":30}
for k,v in d.items():
    print(v)
    if  isinstance(v,list):
        v.append(30)
print(d['a'])
print(d)
print(list(map(lambda x:x*2,l)))
print(["Hello" for i in range(1,10) if i==12])
ly=[]
for i in range(2,100):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        ly.append(i)
print(ly)
#############################INterview questions################
#r=[{"name":"name1", "age":50}, {"name":"name2", "age":25}, {"name":"name3","age":68}, {"name":"name4", "age":10}]

di={'age':50,'age1':30,"age2":25,'age3':43}

# for k,v in di.items():
print(dir(di))

    
 



