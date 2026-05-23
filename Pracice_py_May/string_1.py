# s="puvvada"
# print(dir(s))
# s="abcabccce"
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         print(s[i:j])
#         if len(s[i:j])<4:
#             print("hi",s[i:j])

s="Ramanjaneyulu puvvada"
# l=[]
# d=s.split()
# for i in d:
#     i1=i[::-1]
#     l.append(i1)
# print(" ".join(l))
# def simple(l):
#     l1=[]
#     for i in l:
#         if isinstance(i,list):
#             l1.extend(simple(i))
#         else:
#             l1.append(i)
#     return l1
# l=[1,[2,[3,4],5],6]
# print(simple(l))
# l=[11,2,3]
# print(isinstance("1.0",(int,str)))
# print(dir(s))
#prime program
# n=int(input("enter n number:"))
# for i in range(2,n):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
# print(i)
# x=5
# y=7
# x=x+y#5+7=12
# y=x-y#12-7=5
# x=x-y#12-5=7
#How o perfom prime number
# n=int(input("enter n numbe:"))
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
#     else:
#         print("prime")
# s="B4A1D3"#ABD134
# s1=""
# s2=""
# for i in range(len(s)):
#     if s[i].isalpha():
#         s1=s1+s[i]   
#     else:
#         s2=s[i]+s2
# print(s1,s2)
# t="".join(sorted(s1))
# t1="".join(sorted(s2))
# print(t+t1)
s="abcdfchhujakhskhkkkkkasdkweewwy"
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        print(s[i:j])
    

