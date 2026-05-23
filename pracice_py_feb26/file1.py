# d=[{"name":"name1","age":45},{"name":"name1","age":40},{"name":"My","age":32},{"name":"name1","age":15}]
# d.sort(key=lambda x:x['age'],reverse=True)
# print(d)
# def simple(*ar,**kw):
    
#     print(ar)
#     for  i in kw.values():
#         print(i)
# # simple(1,2,3)
# simple(age=30,name="bal@")
# a=10
# n="balaji"
# for i in ["balaji","omkar","siva","raj","mohan"]:
#     #print(f"hi {i} my age is {a}.")
#     if i=="raj":

#         print(f"hi {i} my age is {30}.")
# n=int(input("enter n number:"))
# d="adult" if n>18 else "not adult"
# print(d)

# s=[i*2 for i in l if i%2==0]
# print(s)

# def simple(*args):
#     t=0
#     for i in args:
#         t=t+i
#     return t
# print(simple(1,2,3,4,10))
# from functools import reduce
# l=[1,2,3,4,5,6]

# l2=reduce (lambda x,y:x*y,list(map(lambda x:x**2,filter(lambda x:x%2==0,l))))
# print(l2)

# class Student:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def simple(self):
#         print(self.a+self.b)
# s=Student(5,10)
# s.simple()
# print(Student.__dict__(s))

data=[100,200,300]
for i in data:
    i=i+50
    print(data,i)



