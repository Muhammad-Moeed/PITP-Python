# Dictonary (Get any value , Get all Keys , items And Values ,
# update any vlaue single and mulitple , pop and delete , clear and delete)
# Memebrship operator in dictonary 



dict1 = {
    'Serial NO' : 1,
    'Name' : 'Moeed',
    'Course': 'Python Programming'
}
print(dict1)
print(dict1['Serial NO']) #Excess value from directly if syntax is wrong so print none
print(dict1.get('Serial NO')) #Excess value from Get Metohd if syntax is wrong so print none

# ***************Get all Keys , items And Values*******************

print(dict1.keys()) #return Keys of dict1
print(dict1.items()) #return Items of dict1
print(dict1.values()) #return Values of dict1

# **************Updating Dictonary dingle updation and multiples updation************

dict2 = {
    'age' : 16,
    'cnic' : 42101-53535435-2
}
print(dict1) #update dict1
dict1.update(dict2)

dict1.update({'updatedKey': 'updated'}) #update dict1 of multpile values directly
print(dict1)

dict1['Course'] = 'PITP Python programming'
print(dict1)

# ***************Pop and Delete and Clear from Dict***************

pop  = dict1.pop('Course') #Pop any delete key from dictnary and return deleted value
print(dict1)
print('Pop value is ', pop )

del dict1['updatedKey'] #del any and all key from dict and no any return value
print(dict1)

# del dict1 
# print(dict1) #//Error 

dict1.clear() # Clear all element and retrun empty dict
print(dict1)


# ***************MemberShip Operator*****************
print('Name' in dict1)

empty = {}
print(type(empty)) # Return type dict


