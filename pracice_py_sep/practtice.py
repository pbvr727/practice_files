# l=[1,2,3,4,5,6,7,8,9,10]
# # print(l[5:]+l[0:5])
# l1=[]

# # for i in range(5,len(l)):
# #     l1.append(l[i])
# # for k in range(0,5):
# #     l1.append(l[k])
# # print(l1)
# l2=[]
# for m in range(len(l)):
#     if m>=5:
#         l1.append(l[m])
#     else:
#         l2.append(l[m])
# print(l1+l2)

# for i in range(8):
#     for j in range(0,i):
#         print(" ",end=" ")
#     for k in range(11-i,i,-1):
#         print("B",end=" ")5q
#     print()
class Student:
    school="MyFamily"
    def __init__(self):
        self.a=100
        self.b=200
    def simple(self):
        print(self.a+self.b)
    @classmethod
    def display(cls):
        print(Student.school)
        cls.school="My1"
        print(cls.school,Student.school)
    @staticmethod
    def display1():
        Student.age=30
        r=200000
        print(Student.age+r)

s=Student()
s.simple()
s.display()
s.display1()
    


    

