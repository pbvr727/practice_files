
import re
# c=0
# p1=re.finditer("Ba","Bala Venkata Ramanjanayeulu"))
# for i in p1:
#     c=c+1
#     print(i.start(),"________",i.end(),"______________",i.group())
# print(c)
#Match will check begining of sring if it is match otherwise None
# p2=re.match("P","Puvvada")
# print(p2)
#fullmatch complete string match then only it will come oherwise return None
# p2=re.fullmatch("Hello Balaji!","Hello Balaji")
# print(p2)
#search it will give first occurence oherwise None
# print(re.search('aj','balajia'))
#Findall will displays ALL occurences of given string
# print(re.findall('hemarama','hemaramaramaramahema'))
####here only iterations numbers will returns
# d=re.finditer(".","OH ! BAlaji123")
# for i in d:
#     print(i.start(),"___",i.group(),"____",i.end())
# s=re.sub("[abcd]","@*!","ced")
# print(s)
# sq=re.subn("[a]","@","Bala Venkata Ramanjaneyulu")
# print(sq)
# sp=re.split("a","Bala Venkata Ramanjaneyulu")
# print(sp)
# f=re.findall("aj+","Balajjji venkata")
# print(f)
# p=re.finditer("a","BalajiBaBal")
# c=0
# for i in p:
#     c=c+1
#     print(i.group())
# print(c)
# ra=re.subn("a","@","balaji727")
# print(ra)
u=re.findall("ab?","aabbiaai yt a")
print(u)




