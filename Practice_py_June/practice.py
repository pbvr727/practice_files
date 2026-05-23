# j=""
# def sum(l,n):
#     global j
#     for i in l:
#         j=i+j
#         print("balaji",j)
#     print(n)
# print("puvvada")
# sum("bala",n="Rani")
################
# import threading
# import time
# def add(x,y):
#     print("addition")

#     print(x+y)
# def sub(y,z):
#     print("substraction")
#     print(time.sleep(1))
#     print(y-z)
# t1=threading.Thread(target=add,args=(10,20))
# t2=threading.Thread(target=sub,args=(20,10))
# t1.start()
# t2.start()
# t1.join();t2.join()
# #####################################
# import threading
# import time

# def add(x, y, result):
#     print("addition")
#     time.sleep(2)
#     result['add'] = x + y

# def sub(y, z, result):
#     print("subtraction")
#     time.sleep(1)
#     result['sub'] = y - z  # Changed to subtraction to match function name

# # Shared dictionary to store results
# results = {}

# t1 = threading.Thread(target=add, args=(10, 20, results))
# t2 = threading.Thread(target=sub, args=(20, 10, results))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# # print("Results:", results)
# d={}
# d1['add']=100
# d['sub']=200;print(d)