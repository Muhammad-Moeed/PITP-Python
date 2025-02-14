# Sets & Metods 
thisset = {"apple", "banana", "cherry", "apple"}

# Add Item
print(thisset)
thisset.add("orange")
print(thisset)
thisset.add("mango")
print(thisset)

# Update 
newset = {'ali',3,True}
thisset.update(newset)
print(thisset)  

# Remove
# Remove "banana" by using the remove() method
# If the item to remove does not exist, remove() will raise an error.

thisset.remove("banana")
print(thisset)

#Discard
#  If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("mango")
print(thisset)

# Pop 
# Remove a random item by using the pop() method:
x = thisset.pop()
print(x)

#Clear #del
thisset.clear()
thisset.clear()
print(thisset)


# Union 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)



