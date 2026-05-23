# # g=[[1,2,3,4],[5,6,1,2]]
# # # output:-
# # # [['1', '2', '3', '4'], ['5', '6', '1', '2']]
# # l=[]
# # for i in g:
# #     for j in i:
# #         l.append(str(j))
# # print(l)
# st = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# # l1=list(filter(lambda s:s%2!=0,st))
# # print(l1)
# # l1=list(map(lambda d:d*d,st))
# # print(l1)
# # p=lambda x,y:x+y
# # print(p(6,7))
# # from functools import reduce
# # d=reduce(lambda y,x:y+x,st)
# # print(d)
# # q=[i for i in st if i%2!=0 ]
# # print(q)
# import re
# pattern=r'^\w{3,6}\d{2}@\w{4}\.[a-z]{3}$'
# x="balaji72@gmail.com"
# m=re.match(pattern,x)
# if m:
#     print("matches")
# else:
s='ABCABCABBCDE balaj'
# #output: A-3,B-4,C-3,D-1,E-1
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
f=""
# l=[]
# for i in s.split():
#     d=i[::-1]
#     l.append(d)
# print(" ".join(l))
# it='B4A1D3'#ot=BBBBADDD
# le=""
# co=""
# for i in range(0,len(it),2):
#     le=it[i]
#     co=co+le*int(it[i+1])
#     print(co)
#     print("".join(co))
l=[10,9,493,0,2,3,8,12,500,6]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
l1=[]
for i in range(len(l)-1,-1,-1):
    l1.append(l[i])
print(l1)




    
    


