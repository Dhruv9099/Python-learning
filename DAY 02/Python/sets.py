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


# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)



# Add Sets
# To add items from another set into the current set, use the update() method.
#Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)