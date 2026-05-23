# class Person:
#     school="MyFAmilyhome"
#     def __init__(self) :
#         pass
#     def simple(self):
#         self.a=10
#     @classmethod
#     def simple1(cls):
#         cls.n=20
#         print(Person.n)
#     @staticmethod
#     def simple3():
#         d=100
#         print(Person.school)
#         print(d)
# p=Person()
# p.simple1()
# p.simple3()
l=[2,4,2,1,2,3,4,5,6,8,7,-1,-10]
l1=l[0]
for i in l:
    if i<=l1:
        i,l1=l1,i
print(l1)
for i in range(len(l)-1,-1,-1):
    print(l[i],end=" ")
import json
s={"name":"balaji","age":30,"Phone":90008,"Married":True}
with open("plain.txt") as f1:
    s1=json.load(f1)
    print(s1)




