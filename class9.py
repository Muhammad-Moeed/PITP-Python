# For in Loop 

# Prime Number
num = 12
if num > 1:
    for i in range(2,num):
            if num%i == 0:
                print('its not a prime number')
                break
            else:
                 print('ITs not a prime number')

# Table of 5
table = int(input("enter num"))
for tab in range(1,11):
     print(table * tab)

#Natural Number
sum = 0 
for i in range(10):
     sum=sum+1
print(sum)

# looping in list and dict

items = [('fruits','apple'),('fruits','banana'),('vegatable','carrot')]
dict ={}

for i in items:
    if i[0] in dict:
      print(dict[i[0]])
    dict[i[0]] = dict[i[0],i[1]]
    print(dict)
else:
     dict[i[0]] = i[1]
     print(dict)

    #Task 01 :
        # Write a program to print list in reverce order
listReverce = [1,2,3,4,5]
reverce = listReverce[::-1]
print(reverce)

    #Task 02 ; 
        #wrtie a program to calculate the length of string without using len

    #Task 03 :
        # Write a program to print maximum value from a list without maximum function

numbers = [0,1,2,7,3,10]
maxvalue = numbers[0]
for num in numbers:
    if num > maxvalue:
        maxvalue = num
print(maxvalue)
    
numbers.sort()
print(numbers)


    

