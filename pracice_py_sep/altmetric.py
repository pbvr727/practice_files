# l="RAMANJANEYULU"
# for i in l:
#     print(i,end="@")
# l=[8,2,1,9,7,6,3,10]
# def simple(l):
#     t=0
#     for i in range(len(l)):
#         print(l[i])
#         t=t+l[i]
#     print("total",t)
# l=[8,2,1,9,7,6,3,10]
# simple(l)
# s="MyFamilyHouse"
# v="aeiouAEIOU"
# for i in s:
#     if i not in v:
#         print(i,end=" ")
s="Puvvada Bala Venkata Ramanjaneyulu"
# l=[]
# for i in s.split():
#     l.append(i[::-1])
# print(" ".join(l))
# # for i in range(len(s)):
#     if i=="a":
s1=s.replace('a','b')
print(dir(s))
l=[1,2,3,4,2,5,6,7,9]
t=15
l1=[]
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]+l[j]==t:
            l1.append([l[i],l[j]])
print(l1)
for k in range(len(l)+1):
    for m in range(len(l)+1):
        print(l[k:m])
l2=[]
for i in range(len(l)-1,-1,-2):
    l2.append(l[i])
print(l2)

print(l[10::-2])
l1=[9,10]
l2=[5,6]
print(l1+l2)
l1.extend(l2)
print(l1)





