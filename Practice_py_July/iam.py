# c="balaji"
# l=len(c)
# c1=0
# for i in range(1,l-1):
#     if c[i]!=c[i-1]:
#         c1=c1+1
# print(c1)
l=[2,3,4,5,7,8,9,11,[89,"Balaj"]]
for i in l:
    if  isinstance(i,list):
        print(i)