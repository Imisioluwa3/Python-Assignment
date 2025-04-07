# 1. Create an empty list called my_list
my_list = []
print(f"Empty List:{my_list}")

# 2. Append 10,20,30,40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(f"List after adding 10,20,30,40:{my_list}")

# 3. Insert 15 at the second index
my_list.insert(1,15)
print(f"List after inserting 15 at index 1:{my_list}")

# 4. Extend my_list with  another list [50,60,70]
another_list = [50,60,70]
my_list.extend(another_list)
print(f"Value of another_list:{another_list}")
print(f"List after extending with another list:{my_list}")

# 5. Remove the last element from my_list
my_list.pop()
print(f"List after removing last element:{my_list}")

# 6. Sort the list in ascending order
my_list.sort()
print(f"Sorted List:{my_list}")

# 7. Find and print the index value of 30
print(f"Index value of 30: {my_list.index(30)}")