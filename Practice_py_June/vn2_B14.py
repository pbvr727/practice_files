##Length of string&Count characters in string
s="puvvada bala venkata ramanjaneyulu"
# c=0
# for i in range(len(s)):
#     c=c+1
# print(c)
#String slicing Small portion &&&Swapping chars in string
print(s[10:20])
# print(s.swapcase());print(s.title());print(s.capitalize())
s1="Yralagadda Reshma Sai"
# print(s+s1);print(.join(s1))
#Substring replacement#Length of longest string in python
# print(s.replace("a",'@',5))
# words = ["apple", "banana", "cherry", "kiwility"]
# words1=len(words[0])
# for i in words:
#     if len(i)>words1:
#         words1=len(i)
#         # print(i,words1)       
# print(i,words1,"ok")
#nth index character from string
# d=5
# print(s[d:len(s)])
#First last chars swapping
# for i in s1:
#     print(s1[0].swapcase())
#     print(s1[-1].swapcase())
# print(i)
# first=s1[0].swapcase()
# last=s1[-1].swapcase()
# middle=s1[1:-1]
# print(first+middle+last)
#Remove odd index values
print(dir(s1))
s1="Yralagadda Reshma Sai"
s2=""
for i in range(len(s1)):
    if i%2!=0:
        print(s2:=s2+s1[i])
#Count words in a string
        c=0

for i in s1.split():
        c=c+1
print(c)
#Sort unique words alphanumerically
# n=input("enter string")
p="night";l=list(p)
p1="thing";l1=list(p1)
for i in range(len(l1)):
     for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
                l1[i],l1[j]=l1[j],l1[i]
print(l1)
def func(l1):
     for i in range(len(l1)):
        for j in range(i+1,len(l1)):
                if l1[i]>l1[j]:
                        l1[i],l1[j]=l1[j],l1[i]
        return l1
# p="night";l=list(p)
# p1="thing";l1=list(p1)
print(func(l1=list("night")))
# print(func(l))
     
     




