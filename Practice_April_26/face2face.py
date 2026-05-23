# s="Welcome to python"
# l1=[]
# for i in s.split():
#     l1.append(i[::-1])
# print(" ".join(l1))
# s1=""
# for i in range(len(s)):
#     s1=s[i]+s1
# print(s1)
# data={'a':["ram",10,20],"b":"20","c":["venki",44]}
# c=0
# for k,v in data.items():
#     if  isinstance(v,(int,list)):
#         c=c+1
# print(c)
#A7B1R3#ABR137
# s="A7B1R3"#ABR137
# s1=""
# s2=""
# for i in s:
#     if i.isalpha():
#         s1=s1+i
#     else:
#         s2=s2+i
        
# print(s1,"numbes",s2)
# s3=sorted(s2)
# s4=sorted(s1)
# print("".join(s4+s3))
#Armstrong number
# for i in range(1,1000):
#     num=i
#     g=len(str(i))
#     r=0
#     c=0
#     while num<0:
#         d=num%10
#         r=r+(d**g)
#         num=num//10
#         c=c+1
# print(c,r)
# print("Hello")
# if r==i:
#     print(r)
#pefect number
# n=int(input("enter n number:"))
# c=0
# for i in range(1,n//2+1):
#     if n%i==0:
#         c=c+i
# if n==c:
#     print("perfect")
# else:
#     print("Not pefect")
# s="aaaabbbaccd"#4a3b2c1
# c=0
# s1=s[0]
# s2=""
# for i in s:
#     if s1==i:
#         c=c+1
#     else:
#         s2=s2+str(c)+s1
#         s1=i
#         c=1
#     print(s2)

# def plain(d):
#     l1=[]
#     for i in d:
#         if isinstance(i,list):
#             l1.extend(plain(i))
#         else:
#             l1.append(i)
#     return l1
# d=[1,[2,3],5,[6,7,8]]
# print(plain(d))
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         result=n*fact(n-1)
#     return result
# print(fact(8))
d={"a":[],"b":[],"c":[]}
for i in range(1,10):
    d['a'].append(i)
    if i%2==0 or i%3==0:
        d['b'].append(i)
print(d)
for k,v in zip(d['a'],d['b']):
    d['c'].append(k*v)
print(d)
l=[0,3,1,4,3,7,6,9,2]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]*l[j]==12:
            print(l[i],l[j])
    






 