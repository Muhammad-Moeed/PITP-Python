# how to claculate the sum of arthematic series from 1 to N 

def arthRecursion(firstterm, dif, num):
    if num==0:
        return 0
    else:
        return firstterm + arthRecursion(firstterm + dif, dif, num-1)
                                            #1     +  2,   2 ,  2
print(arthRecursion(1,2,3))

# Tuple 
t = (1,2,3,4,5,8,6)
t.index(4)
t.count(3)

# write a python program to replace last value of tuples in a list using replace metohd
# sample [(1,2,3),(4,5,6),(7,8,9)]
# output [(1,2,10),(4,5,10),(7,8,10)]


def replace_last_value(lst):
    return [tuple(i[:-1] + (10,)) for i in lst]
replace_last_value([(1,2,3),(4,5,6),(7,8,9)])
# OR 
sample = [(1,2,3),(4,5,6),(7,8,9)]
new = []
for x in sample:
    a=list(x)
    a[-1] =10
    b = tuple(a)
    new.append(b)
print(new)
     