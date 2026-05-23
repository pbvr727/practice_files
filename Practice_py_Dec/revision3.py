# for i in range(10):
#     if i==9:
#         print(i)
#         break
#     print("Hello")
from itertools import permutations, combinations

items = [1, 2, 3]

print(list(permutations(items, 3)))
print(list(combinations(items, 3)))

# print("Balaji")
# import random
# d=random.randint(100000,1000000)
# print(d)
# n=int(input("enter n number"))
# n1="Authentication success" if n==d else "NOt Authenication"
# print(n1)
# n="thing"
# n1=n[0]
# n2=sorted(n)
# print(n2)
# l=[2,1,3,8,4,5,6,9]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
# f="balaji"
# for i in range(len(f))
# n2=sorted(n)
# n3=sorted(n1)
# n4="Anagrams" if n2==n3 else "Not Anagram"
# print(n4)
class School:
    school_name="MyFamilyHighSchool"
    visit=0
    def __init__(self):
        self.sname=[]
    def simple(self,name):
        self.sname.append(name)
        print(self.sname)
        School.visit=School.visit+1
        print(School.visit)
s=School()
s.simple('Balaji')
s.simple("Omkar")
s1=School()
s1.simple("Balaji")