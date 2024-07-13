
# python program to print table of number which is lies between 1 to 10
        # python program to print table of number which is lies between 1 to 10
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} X {j} = {i*j}')
#     print()

# for k in range(1,20):
#     print("K values", k)
#     # Nested loop example:
#     for  l in range(k+1):
#         print("l", l)
# print(type(l))

for i in range(3,4):
    for j in range(1,11):
        print(f"{i} X {j} === {i*j}")


# How would you remove duplicate elements from a list while preserving the order?
# You can use a `for` loop along with a set to remove duplicates while preserving the order:

my_list = [1, 2, 3, 2, 1, 3, 1, 1, 2, 3, 4, 5]
unique_list = []
seen = set()

for item in my_list:
    if item not in seen:
        unique_list.append(item)
        seen.add(item)
        print("uniquelist: ",unique_list)
        print("seen: ",seen)