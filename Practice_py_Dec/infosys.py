# def decor(func):
#     def wrapper(*a,**b):
#         for i in a:
#             print(i)
#         for k,l in b.items():
#             print(k,":",l)
#         return func(a,b)
#     return wrapper

# @decor
# def fun(a,b):
#     print("Hello")
#     c=a+b
# print(fun(10,10))


def timer(func):
    def wrapper(name):
        print("start...")
        func(name)            # only works if func takes NO arguments!
        print("end...")
    return wrapper

@timer
def hello(name):          # This will CRASH!
    print("Hi", name)

hello("Alice")  # TypeError: wrapper() takes 0 positional arguments but 1 was given


# def decor(func):
#     def inner(*args,**kw):
#         print("Hello Decorator")
#         result=func(*args,**kw)
#         print("End Decorator")
#         return result
#     return inner


# @decor
# def greet():
#     print("Hello greet me everyhing")
#     print()
# greet(30,y=20)
# greet(6,)


# import datetime
# def decor(fun):
#     def inner(*r,y):
#         stat=datetime.datetime.now()
#         resul=fun(r,y)
#         end=datetime.datetime.now()
#         return end-stat,resul
#     return inner


# @decor
# def greet(n,u):
#     l=[]
#     print(n+u)
#     for i in range(2,n+1):
#         for j in range(2,int(i**0.5)+1):
#             print("i",i,"j",j)
#             if i%j==0:
#                 break
#         else:
#             l.append(i)
#     return l
# print(greet(100,9))


def simple(n):
    for i in range(n):
        yield i
n1=simple(10) 
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())
print(n1.__next__())

a=30
b=30
print(id(a));print(id(b))
print(a is b)
print(a==b)

l=[1,2,3,4,5]
l1=iter(l)
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
# print(next(l1))
# print(next(l1))

# g=lambda x,y:x+y
# print(g(90,10))
# l=[i for i in range(1,10) if i%2!=0]

# print(l)
# l=[2,6,5,0,23,45,60]
# print(list(map(lambda x:x*2,l)))
# print(list(filter(lambda x:x%2==0,l)))
# from functools import reduce
# q=reduce(lambda x,y:x+y,l)
# print(q)
##########oops##############333