# **********************************For in Loop tsks******************************************        

            # Task # 1
list = [1,'a',2,'b',3,'c',4,'d',5,'e']

list.extend([12,'p',19,'r'])
print('List 1 is ',list)

list.pop()
list.pop()
list.pop()
list.pop()
print('list 2 is :',list)

list.insert(3,'x')
list.insert(4,11)
list.insert(5,'y')
list.insert(6,12)
list.pop(7)
list.pop(8)
list.pop(7)
list.pop(7)
print('list 4 is :',list)

list.pop(0)
list.pop(0)
list.insert(1,'b')
list.insert(2,3)
list.insert(3,'c')
list.insert(4,4)
list.insert(5,'d')
list.insert(6,5)
list.insert(7,'e')
list.pop(8)
list.pop(8)
list.pop(8)
list.pop(8)
list.pop(8)
list.pop(8)
list.pop(8)
print('List 5 is :',list)



list.clear()
print('List 3 is :',list)


# ***********************While loop******************

# i = 15
# while i > 0:
#   print(i)
#   i -= 1

#   ynativ

# i = 1
# while i <= 5 :
#   print(i)
#   i += 1

# i = 1
# while i<=10:
#     if i%2 == 0:
#         print('it even ')
#     print(i)


# num = 100
# while num<500:
#     if num%11 ==0:
#         print(num)
# print(num)

for i in range(100,500):
    if  i%11 ==0 and i%2!=0:
        print(i)







