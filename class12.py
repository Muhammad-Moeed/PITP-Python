list=[1,2,3,4,5]
print(len(list))
for i in range(len(list)-1,-1,-1):
    print(list)

list1=[1,2,3,4,5]
lst=[]
for i in reversed(list1):
    lst.append(i)
print(lst)

n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)


string='apple'
count=0
for i in string:
    count+=1
print (count)

lst1=[1,2,3,4,5,6]
for i in lst1:
    print(i**2)
    print(f'the square of number {i} is {i**2}')