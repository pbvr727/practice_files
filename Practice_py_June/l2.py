for i in range(10):
    for j in range(10-i):
        print(" ",end="")
    for k in range(i+1):
        print(chr(k+65),end=" ")
    for l in range(i):
        print("B@lu",end=" ")
    print()
#################################################
s="Puvvada Bala Venkata Ramanjaneyulu"
l=list(s)
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[i]<l[j+1]:
            l[i],l[j+1]=l[j+1],l[i]
print("".join(l))
####################################
s="Puvvada Bala Venkata Ramanjaneyulu"
s1=s.split()
j=[]
for i in s1:
    j.append(i[::-1])

print(" ".join(j))
###################################################
# def add(x):
#         if x==0:
#             return 1
#         else:
#             return x+add(x-1)

# print(add(6))
##########################################
# d=dict(c=100,a=100,b=100)
# print(d)
l=[2,5,1,33,4,5,6]
# l1=[]
# for i in range(len(l)-1,-1,-1):
#     l1.append(l[i])
# print(l1)
# l1=l[0]
# for i in l:
#     if i<l1:
#         l1=i
# print(l1)
# print(list(map(lambda x:x*2,l)))
# print(list(filter(lambda x:x%2==0,l)))
# from functools import reduce
# print(reduce(lambda x,y:x*y,l))
# x=20;y=10
# x=x^y
# y=x^y
# x=x^y
# print(x,y)
# def add(*args,**kwargs):
#     k=0
#     for i in args:
#         print(k:=k+i)
#     for k,v in kwargs.items():
#         print(k,v)
# print(add(5,20,30,50,b=90,c=92))
# s="puvvada bala venkata ramanjaneyulu"
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         print(s[i:j])
s = "puvvada bala venkata ramanjaneyulu"

# def longest_unique_substring(s):
#     start = 0
#     max_len = 0
#     max_substr = ""
#     seen = {}

#     for end in range(len(s)):
#         char = s[end]
#         if char in seen and seen[char] >= start:
#             start = seen[char] + 1
#         seen[char] = end
#         if end - start + 1 > max_len:
#             max_len = end - start + 1
#             max_substr = s[start:end+1]

#     return max_substr

# print("Longest substring without repeating characters:")
# print(longest_unique_substring(s))
# # s="balaji"
# start=0
# end=0
# dic={}
# for i in range(len(s)):
#     d=s[i]
#     if d in dic and s[i]>=start:
#         start=s[i]+1
#     s[i]=end
#     if 
#         print(s[i:j])
#         print(s[i:j])
s = "puvvada bala venkata ramanjaneyulu"
print(s[:-2])
s1="racecar"
d=""
for i in s1:
    d=i+d
print(d)
if s1==d:
    print("palindome")
else:
    print("not palindrome")



