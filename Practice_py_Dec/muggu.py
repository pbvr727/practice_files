# for i in range(1,9):
#     for j in range(9,i,-1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()
# l=[]
# n=int(input("enter n number:"))
# for i in range(2,n):
#     for j in range(2,int(i*0.5)+1):
#         if i%j==0:
#             break
#     else:
#         l.append(i)
# print(l)


def rec(l):
    l1=[]
    for i in l:
        if  isinstance(i,list):
            l1.extend(rec(i))
        else:
            l1.append(i)
    return l1
l=[1,2,[3,4,5],6,[7,8]]
print(rec(l))
