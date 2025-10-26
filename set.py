import copy

# ---------------------------
# Creating a set and basic operations
# ---------------------------
my_set = {100, 20, 3, 4, 5, 6}
print("Original set:", my_set)

# Adding elements
my_set.add(4)  # duplicates are ignored
print("After adding 4:", my_set)

my_set.add(390)
print("After adding 390:", my_set)

# Removing elements
my_set.remove(3)  # KeyError if not present
print("After removing 3:", my_set)

my_set.discard(500)  # does not raise error if element not present
print("After discarding 500:", my_set)

# Pop element (removes arbitrary element)
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("Set after pop:", my_set)

# Union, Intersection, Difference
set_a = {1,2,3}
set_b = {3,4,5}

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (a-b):", set_a - set_b)

# Check membership
print("Is 2 in set_a?", 2 in set_a)
print("Is 5 in set_a?", 5 in set_a)

# Length, min, max, sum
print("Length of my_set:", len(my_set))
print("Min:", min(my_set))
print("Max:", max(my_set))
print("Sum:", sum(my_set))

# ---------------------------
# Set comprehensions
# ---------------------------
numbers = {x for x in range(1,7)}
print("Numbers set:", numbers)

squares = {x**2 for x in range(1,7)}
print("Squares set:", squares)

# Deep copy (technically same as shallow copy for set of immutable elements)
copy_of_squares = copy.deepcopy(squares)
print("Deep copy of squares:", copy_of_squares)

# ---------------------------
# Difference between shallow and deep copy for sets with mutable elements
# ---------------------------
matrix_set = {frozenset([1,2]), frozenset([3,4])}  # must use frozenset because set cannot contain list
shallow_copy_set = matrix_set.copy()
deep_copy_set = copy.deepcopy(matrix_set)

print("matrix_set:", matrix_set)
print("shallow_copy_set:", shallow_copy_set)
print("deep_copy_set:", deep_copy_set)

# Cannot modify frozenset directly (immutable), so demonstrating add/remove with outer set
matrix_set.add(frozenset([5,6]))
print("After adding frozenset([5,6]) to matrix_set:", matrix_set)
print("shallow_copy_set:", shallow_copy_set)  # shallow copy does not have new element
print("deep_copy_set:", deep_copy_set)        # deep copy does not have new element

# ---------------------------
# Ways to create shallow copy of a set
# ---------------------------
set1 = {"asit"}
print("set1:", set1)

set2 = copy.copy(set1)
print("Shallow copy using copy.copy():", set2)

set3 = set1.copy()
print("Shallow copy using set.copy():", set3)



# | **Operation**           | **List**                                | **Set**              | **Notes**                                                     |
# | ----------------------- | --------------------------------------- | -------------------- | ------------------------------------------------------------- |
# | Add element             | `append(x)`                             | `add(x)`             | Adds a single element. Duplicates ignored in sets.            |
# | Add multiple            | `extend([x,y])`                         | `update([x,y])`      | Adds multiple elements at once.                               |
# | Remove element          | `remove(x)`                             | `remove(x)`          | Raises error if element not found.                            |
# | Remove element safely   | N/A                                     | `discard(x)`         | Does **not** raise error if element not found.                |
# | Remove by index         | `pop(i)`                                | `pop()`              | Removes **arbitrary** element in sets (no indexing).          |


