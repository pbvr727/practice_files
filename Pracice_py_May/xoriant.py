#oops
# class Person:
#     d=100
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         Person.d=101
#     def simple(self):
#         print(self.a,self.b,Person.d)
#     def simple1():
#         print("Hello")
# p=Person(10,20)
# p.simple()
# a=Person(20,100)
# Person.d=102
# print(a.d)
# print(p.d)
# print(Person.__dict__)
# print(a.__dict__)
s=input("enter string1:")
l=list(s)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
        
s1=input("enter sring:")
l1=list(s1)
for i1 in range(len(l1)):
    for j1 in range(i1+1,len(l1)):
        if l1[i1]>l1[j1]:
            l1[i1],l1[j1]=l1[j1],l1[i1]
print(l1)
if l==l1:
    print("Anagram")
else:
    print("not anagram")