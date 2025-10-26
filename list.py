import sys

my_list = [100, 20,3,4,5,6]


print(my_list)

my_list.append(4)
print(my_list)

my_list.remove(3)       # remove the first occurrence of element, error if that element is not in that list
print(my_list)

my_list.insert(2,1000)
print(my_list)


my_list.pop(3)      # remove the object at that index
print(my_list)


my_list.sort()
print(my_list)

my_list.extend([1,1,1])     # adds those elements to the end of the list
print(my_list)

print(my_list.index(4))  # prints the index of first occurence if 4, error if 4 not in list

print(my_list.count(1))     # frequency of 1


my_list.reverse()
print(my_list)


new_list = my_list.copy()
print(new_list)         # shallow copy of list is returned


new_list.remove(4)      # will not be removed from original list as integers are immutable
print(f"new_list:{new_list}")
print(f"my_list:{my_list}")


new_list.append(390)    # will only be appended in new_list again for the same reason
print(f"new_list:{new_list}")
print(f"my_list:{my_list}")



# understand that only the reference from the shallow copy is removed
list_of_list = [[1,2],[2,3],[3,4],[4,5]]
shallow_copy= list_of_list.copy()

print(f"list_of_list:{list_of_list}")
print(f"shallow_copy:{shallow_copy}")


shallow_copy.remove([1,2])

print(f"list_of_list:{list_of_list}")
print(f"shallow_copy:{shallow_copy}")

# but if we remove the object itself from the original list

target = list_of_list[2]
ref_count=sys.getrefcount(target)
print(f"ref count of [3,4] before deletion from list_of_list:{ref_count-2}" )

list_of_list.remove([3,4])
print(f"list_of_list:{list_of_list}")
print(f"shallow_copy:{shallow_copy}")

# the actual object does not get deleted because its ref count is not 0 yet, due to shallow copy having a linking to it

ref_count=sys.getrefcount(target)
print(f"ref count of [3,4] after deletion from list_of_list:{ref_count-2}" )


my_list[0]=22
print(f"new_list:{new_list}")
print(f"my_list:{my_list}")