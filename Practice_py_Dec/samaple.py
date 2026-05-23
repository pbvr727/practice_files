print("Heolllo welcome to python")
l=[-10,0,3,1,4,3,7,6,9,2,100]
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]+l[j]==5:
            print(i,j)
            print(l[i],l[j],"values")
max=l[0]
for i in range(len(l)):
    if l[i]<max:
        max=l[i]
print(max)

# students = [{"name": "Alice", "grades": [85, 90, 78]},
# {"name": "Bob", "grades": [65, 70, 72]},
# {"name": "Charlie", "grades": [95, 92, 88]},] 
# threshold = 80 
# for i in students:
#     if sum(i["grades"])//len(i["grades"])>threshold:
#         print(i["name"])
inventory = { "item_1": {"quantity": 5, "price": 10.99},     "item_2": {"quantity": 3, "price": 20.50},     "item_3": {"quantity": 10, "price": 5.25}, } 
    
for k,i in inventory.items():
    print(k,":",i['quantity']*i['price'])
activities = {"user_1": {"login", "purchase", "logout"},"user_2": {"login", "browse","logout"},"user_3": {"browse", "purchase"}, } 
for i in range(len(activities)):
    for j in range(i+1,len(activities)+1):
        if activities[i]!=activities[j]:
            print(activities[i].intersection(activities[j]))
 


