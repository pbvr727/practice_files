s="python is easy"
#nothyp si ysae
j=""
# for i in s.split():
#     j=j+i[::-1]+" "
# print(j)
# l1=[]
# for i in s.split():
#     l1.append(i[::-1])
# print(" ".join(l1))
##############################################
l=[1,1,2,2,3,3,4,4,5,6,7,7,"h"]

print([i for i in range(len(l)) if l.count(i)==1 ])
data={'a':["ram",10,20],"b":[20],"c":["venki",44]}
print(len(data.values()))
c=0
for i in data.values():
    if isinstance(i,list):
        c=c+1
print(c)
#######################################
# d=list("aeiou")
# c=0
# for i in (s:=input("Enter string Name")):
#     if i in d:
#         c=c+1
# print(c)
#######################################################
#String Reverse
# s="Ramanjaneyulu"
# i=0
# p=""
# while i<len(s):
#     p=s[i]+p
#     i=i+1
# print(p)
# s="puvvada bala puvvada balaji puvvada bala bala"
# s1=s.split()
# d={}
# for i in s1:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
#############################################
#A7B1R3#ABR137
# s="A7B1R3"
# s1=""
# c=""
# for i in range(0,len(s)):
#     if s[i].isalpha():
#         s1=s[i]+s1
#     else:
#         c=s[i]+c
# s2=sorted(s1)
# s3=sorted(c)
# print(s2+s3)
# print("".join(s2+s3))
################################################3
#Print armstong numbers 1 to 999
for n in range(1,1000):
    temp=n
    r=0
    x=len(str(n))
    while 0<n:
        d=n%10
        r+=d**x
        n=n//10
    if temp==r:
        print(temp)
############################################
#  Check Perfect Number
n=25
s=0
for i in range(1,n):
       
        if n%i==0:
            print(n,i,end=" ")
            s=s+i
            print(s,"count")
if s==n:
    print("perfect number")
else:
     print("not pefect")
######################################
# ip="a5b3c4"#op-aaabbcccc
# s=""
# s1=""
# s2=""
# for i in range(0,len(ip)):
#     if ip[i].isalpha():
#         s=ip[i]
#         print(s)
#     else:
#         s1=s*int(ip[i])
#         s2=s2+s1
# print(s2)
########################################################
# s="aaaabbbccd"#4a3b2c1
# s1=s[0]
# c=0
# op=""
# for i in s:
#     if i==s1:
#         c=c+1
        
#     else:
#         op=op+str(c)+s1
#         c=1
#         s1=i
# print(op)
##########################################################
#fibancoic seies
# a,b=0,1
# for i in range(11):
#     a,b=b,a+b
#     print(b)
####################
# l1=[1,2,4,5,6,8]
# print([i for i in range(10) if i not in l1])  
#################################################3
#Without iterating for loop can we print
# l=eval(input("enter Dynamic List Elements:"))
# start=eval()    
# l=eval(input("enter elements"))
# print(type(l))
# start=eval(input("Enter elements:"))
# end=eval(input("enterd end elemnts"))
# def simple(l,start,end):
#     if  start>=end:  
#         return
#     print(l[start])
#     simple(l,start+1,end)
# simple(l,start,end)
# s="Puvvada Bala Venkata Ramanjaneyulu"
# i=0
# while i<len(s):
#     print(s[i],end="\t")
#     i=i+1


# def simple3(l):
#     l1=[]
#     for i in l:
#         if isinstance(i,list):
#             l1.extend(simple3(i))
#         else:
#             l1.append(i)
#     return l1
# l=[1,[2,3],4,[5,6,7],9]
# print(simple3(l))
# def fact(n):
#     if n==7:
#         return 1
#     else:
#         return n*fact(n+1)
# print(fact(5))
#####################################################
# d={"a":[],"b":[]}
# for i in range(5):
#     d['a'].append(i)
#     d["b"].append(i)
# print(d)
# for k,y in zip(d['a'],d['b']):
#     print(k*y)
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return fact(n)*fact(n-1)
# print(fact(5))
ip="a5b3c4"#op-aaabbcccc
s="";s1="";s2=""
for i in ip:
    if i.isalpha():
        s=i
    else:
        s1=s*int(i)
        s2=s2+s1
print(s2)





    




        





