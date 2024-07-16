# Python Sets
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, unindexed, and Duplicates Not Allowed
# Set items can be of any data type: string, integer, float, boolean etc., even None.
#Once a set is created, you cannot change its items, but you can add new items.
myset = { "banana","apple", "banana", "cherry", "cherry"}
print(myset)

thissset = {"apple", "banana", "cherry", True, 2,1}
print(thissset)

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
print(len(thisset))



#  access items
for x in thisset:
    print("access item via for loop: ",x)


# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("checK if banana is present True or False")
print("banana" in thisset)


# Check if "banana" is NOT present in the set:

print("checK if banana is NOT present True or False")
print("banana" not in thisset)
# Add an item to a set, using the add() method:

thisset.add("orange")
print("thisset.add(""orange"") : ")
print(thisset)

# Add Sets
# To add items from another set into the current set, use the update() method.
#Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# It is also possible to use the set() constructor to make a set.
set1= set((1,2,3)) 
print(set1) 
# output: {1,2,3}


# To remove an item in a set, use the remove(), or the discard() method.
thisset.remove("banana")
print(thisset)

# Remove "mango" by using the discard() method:
thisset.discard("mango")
print(thisset)


# Remove a random item by using the pop() method:
x=thisset.pop()
print(thisset)

# The clear() method empties the set:

thisset.clear()
print(thisset)

# The del keyword will delete the set completely:

# del thisset
print(thisset)



# ------------ 

# union() and | same
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.union(y) 
print(z)

set3= x | y
print("set3:\n " ,set3)



# join multiple set
myset=set1.union(thisset,x,y,set3)
print("myset \n ", myset)

# Join a Set and a Tuple
tup=(1,522,25,62)
set_tup_union= set3.union(tup)

print("set_tup_union \n ", set_tup_union)


# ------------
# intersection() and & same
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.intersection(y) 
print(z)

set4=x & y
print("set4\n " ,set4)



# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
print("x: " ,x)
print("y: ",y)
x.intersection_update(y)

print(x)

#  
z=x.intersection(y)
print("z : ",z)



# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
one={1,2,3,4,3,5}
two={2,3,4,5,6,7}
three = one.difference(two)
print("three using one.difference(two): ", three)
four= two.difference(one)
print("four using two.difference(one): ", four)



oo= 4 + 3 % 5
print(oo)


























"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""