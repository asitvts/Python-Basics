formattedString.py
---

entire readme is gpt generated (i have no shame)

````markdown
# String Formatting in Python

This script demonstrates **different ways to combine strings** (specifically a first and last name) in Python using various formatting techniques.

---

## 🧩 Code Overview

```python
first_name = "asit"
last_name = "vats"

full_name = "{} {}"

print("asit " + last_name)
print(f"asit {last_name}")
print(full_name.format(first_name, last_name))
````

---

## 🧠 Explanation

| Method                                  | Description                                                  | Example Output |
| --------------------------------------- | ------------------------------------------------------------ | -------------- |
| **String Concatenation** (`+`)          | Joins strings using the `+` operator.                        | `asit vats`    |
| **f-string (formatted string literal)** | Introduced in Python 3.6+, allows inline variable embedding. | `asit vats`    |
| **`str.format()` method**               | Uses placeholders `{}` to insert variables into a string.    | `asit vats`    |

---

## ▶️ How to Run

1. Save the script as `formattedString.py`.
2. Open a terminal in the project folder.
3. Run the following command:

```bash
python3 formattedString.py
```

---

## 🧾 Output

```
asit vats
asit vats
asit vats
```

---

## 📚 Learn More

* [Python String Formatting Docs](https://docs.python.org/3/library/string.html#format-string-syntax)
* [f-strings in Python](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)



# list.py




````markdown
# 🐍 Python List Operations and Copying Concepts

This script demonstrates **fundamental and advanced Python list operations**, including **mutation**, **slicing**, **comprehensions**, and the difference between **shallow** and **deep copies**.

---

## 📘 Topics Covered

### 1. Basic List Operations
```python
my_list = [100, 20, 3, 4, 5, 6]
````

| Method             | Description                                              | Example                   |
| ------------------ | -------------------------------------------------------- | ------------------------- |
| `append(x)`        | Adds an element to the end of the list                   | `my_list.append(4)`       |
| `remove(x)`        | Removes the first occurrence of `x` (error if not found) | `my_list.remove(3)`       |
| `insert(i, x)`     | Inserts `x` at index `i`                                 | `my_list.insert(2, 1000)` |
| `pop(i)`           | Removes element at index `i`                             | `my_list.pop(3)`          |
| `sort()`           | Sorts list in ascending order                            | `my_list.sort()`          |
| `extend(iterable)` | Adds multiple elements at once                           | `my_list.extend([1,1,1])` |
| `index(x)`         | Returns first index of `x`                               | `my_list.index(4)`        |
| `count(x)`         | Counts frequency of `x`                                  | `my_list.count(1)`        |
| `reverse()`        | Reverses list in place                                   | `my_list.reverse()`       |

---

### 2. Copying Lists

| Type             | Method                      | Description                                            |
| ---------------- | --------------------------- | ------------------------------------------------------ |
| **Shallow Copy** | `new_list = my_list.copy()` | Creates a new list, but references same inner objects. |
| **Deep Copy**    | `copy.deepcopy(obj)`        | Recursively copies all objects (no shared references). |

#### Example:

```python
import copy
matrix = [[1,2], [3,4]]
shallow_mat = matrix.copy()
deep_mat = copy.deepcopy(matrix)

matrix[0][0] = 100
```

**Output:**

```
matrix       : [[100, 2], [3, 4]]
shallow_mat  : [[100, 2], [3, 4]]   # shares reference
deep_mat     : [[1, 2], [3, 4]]     # independent
```

---

### 3. Shallow Copy and Reference Behavior

Python lists store **references** to objects, not the objects themselves.
This is why changes to **mutable objects** (like lists) reflect across shallow copies.

```python
list_of_list = [[1,2], [2,3], [3,4], [4,5]]
shallow_copy = list_of_list.copy()

# Removing an element
shallow_copy.remove([1,2])

# Both lists still share the same inner objects
```

---

### 4. Checking Object References

Using the `sys` module:

```python
import sys
target = list_of_list[2]
print(sys.getrefcount(target))
```

This shows how many active references exist to an object —
objects are deleted only when reference count drops to `0`.

---

### 5. Useful Built-in List Functions

| Function       | Description                 |
| -------------- | --------------------------- |
| `len(my_list)` | Number of elements          |
| `sum(my_list)` | Sum of all numeric elements |
| `max(my_list)` | Largest element             |
| `min(my_list)` | Smallest element            |

---

### 6. List Slicing

```python
my_list[1:4]    # Elements from index 1 to 3
my_list[::-1]   # Reverse list
```

---

### 7. List Comprehensions

Quick way to generate lists dynamically:

```python
numbers = [x for x in range(1,7)]
squares = [x**2 for x in range(1,7)]
```

Output:

```
[1, 2, 3, 4, 5, 6]
[1, 4, 9, 16, 25, 36]
```

---

### 8. Creating Shallow Copies (Multiple Ways)

```python
import copy
list1 = ["asit"]
list2 = copy.copy(list1)
list3 = list1.copy()
list4 = list1[:]
```

All of the above create **shallow copies** of `list1`.

---

## 🧠 Key Takeaways

* **Mutable objects** (like lists, dicts) share references under shallow copy.
* **Immutable objects** (like int, str, tuple) don’t share state even in shallow copies.
* Use `copy.deepcopy()` when you need a completely independent copy.
* Understand **reference behavior** to avoid unexpected side effects.

---

## ▶️ How to Run

1. Save the script as `list_operations.py`
2. Open a terminal and navigate to the folder.
3. Run:

```bash
python3 list_operations.py
```

---

## 📚 Additional References

* [Python Lists Documentation](https://docs.python.org/3/tutorial/datastructures.html)
* [copy module — shallow and deep copy](https://docs.python.org/3/library/copy.html)
* [sys.getrefcount()](https://docs.python.org/3/library/sys.html#sys.getrefcount)



set.py
---

````markdown
# 🧮 Python Set Operations and Copying Concepts

This script demonstrates **fundamental and advanced operations on Python sets**, including **creation**, **modification**, **set algebra (union, intersection, difference)**, **set comprehensions**, and **copying behavior**.

---

## 📘 Topics Covered

### 1. Creating and Manipulating Sets

```python
my_set = {100, 20, 3, 4, 5, 6}
````

| Operation          | Method       | Description                                                              |
| ------------------ | ------------ | ------------------------------------------------------------------------ |
| **Add element**    | `add(x)`     | Adds an element to the set. Ignores duplicates.                          |
| **Remove element** | `remove(x)`  | Removes element `x`; raises `KeyError` if not found.                     |
| **Safe remove**    | `discard(x)` | Removes element `x` if present; no error if missing.                     |
| **Pop**            | `pop()`      | Removes and returns an **arbitrary** element (since sets are unordered). |

#### Example:

```python
my_set.add(4)
my_set.discard(500)
popped_element = my_set.pop()
```

---

### 2. Set Algebra (Mathematical Operations)

```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}
```

| Operation        | Symbol | Example         | Result   |        |                   |
| ---------------- | ------ | --------------- | -------- | ------ | ----------------- |
| **Union**        | `      | `               | `set_a   | set_b` | `{1, 2, 3, 4, 5}` |
| **Intersection** | `&`    | `set_a & set_b` | `{3}`    |        |                   |
| **Difference**   | `-`    | `set_a - set_b` | `{1, 2}` |        |                   |

---

### 3. Membership and Built-in Functions

| Function          | Description                 | Example Output      |
| ----------------- | --------------------------- | ------------------- |
| `in`              | Check membership            | `2 in set_a → True` |
| `len()`           | Number of elements          | `len(my_set)`       |
| `min()` / `max()` | Smallest / Largest element  | `min(my_set)`       |
| `sum()`           | Sum of all numeric elements | `sum(my_set)`       |

---

### 4. Set Comprehensions

Just like list comprehensions, but create sets instead:

```python
numbers = {x for x in range(1,7)}
squares = {x**2 for x in range(1,7)}
```

**Output:**

```
Numbers set: {1, 2, 3, 4, 5, 6}
Squares set: {1, 4, 9, 16, 25, 36}
```

---

### 5. Copying Sets

| Type             | Example               | Description                                                                            |
| ---------------- | --------------------- | -------------------------------------------------------------------------------------- |
| **Shallow Copy** | `set2 = set1.copy()`  | Creates a new set with same elements.                                                  |
| **Deep Copy**    | `copy.deepcopy(set1)` | Fully copies nested or mutable structures (not usually needed for sets of immutables). |

#### Example:

```python
import copy
copy_of_squares = copy.deepcopy(squares)
```

---

### 6. Sets with Mutable Elements — Using `frozenset`

Sets cannot contain **mutable elements** like lists.
To store “set-like” structures inside a set, use `frozenset` (an immutable set).

```python
matrix_set = {frozenset([1,2]), frozenset([3,4])}
```

Then you can safely perform copies:

```python
shallow_copy_set = matrix_set.copy()
deep_copy_set = copy.deepcopy(matrix_set)
```

Adding a new element:

```python
matrix_set.add(frozenset([5,6]))
```

**Output:**

```
matrix_set: {frozenset({1,2}), frozenset({3,4}), frozenset({5,6})}
shallow_copy_set: {frozenset({1,2}), frozenset({3,4})}
deep_copy_set: {frozenset({1,2}), frozenset({3,4})}
```

---

### 7. Creating Shallow Copies (Multiple Ways)

```python
import copy
set1 = {"asit"}
set2 = copy.copy(set1)    # using copy module
set3 = set1.copy()        # using set's built-in method
```

All of the above create **shallow copies**.

---

### 8. Comparison Between List and Set Operations

| **Operation**         | **List**                | **Set**         | **Notes**                                    |
| --------------------- | ----------------------- | --------------- | -------------------------------------------- |
| Add element           | `append(x)`             | `add(x)`        | Sets ignore duplicates                       |
| Add multiple elements | `extend([x,y])`         | `update([x,y])` | Adds all elements from iterable              |
| Remove element        | `remove(x)`             | `remove(x)`     | Both raise error if missing                  |
| Safe remove           | ❌                       | `discard(x)`    | Prevents error if not found                  |
| Remove by index       | `pop(i)`                | `pop()`         | Set removes **arbitrary** element (no index) |
| Ordering              | ✅ Ordered (since Py3.7) | ❌ Unordered     | Sets have no guaranteed order                |
| Allows duplicates     | ✅ Yes                   | ❌ No            | Unique values only in sets                   |

---

## 🧠 Key Takeaways

* **Sets** are **unordered collections of unique elements**.
* They support **mathematical set operations** like union, intersection, and difference.
* **frozenset** allows storing immutable sets inside sets.
* **Shallow and deep copies** behave similarly for sets of immutable elements.
* Use sets when you need **fast membership checks** and **uniqueness**.

---

## ▶️ How to Run

1. Save the file as `set_operations.py`
2. Open your terminal and navigate to the folder.
3. Run:

```bash
python3 set_operations.py
```

---

## 📚 References

* [Python Sets — Official Docs](https://docs.python.org/3/library/stdtypes.html#set)
* [frozenset type](https://docs.python.org/3/library/stdtypes.html#frozenset)
* [copy module](https://docs.python.org/3/library/copy.html)



dict.py
---

````markdown
# 📘 Python Dictionary Operations and Manipulation

This script demonstrates **essential and intermediate-level Python dictionary operations**, including **accessing keys/values**, **iterating**, **updating**, **copying**, and **removing items** from dictionaries.

---

## 🧩 What is a Dictionary?

A **dictionary** in Python is an **unordered collection of key-value pairs**.  
Each key is **unique** and **immutable** (strings, numbers, or tuples), while values can be of any type.

```python
my_dict = {
    "name": "asit",
    "age": 22,
    "salary": 100.50,
    "has_6_pack_abs": False
}
````

---

## 🧠 1. Accessing Values

| Method                        | Description                                  | Example                       | Output |
| ----------------------------- | -------------------------------------------- | ----------------------------- | ------ |
| `my_dict["key"]`              | Direct access; raises `KeyError` if missing  | `my_dict["name"]`             | `asit` |
| `my_dict.get("key")`          | Safe access; returns `None` if key not found | `my_dict.get("gender")`       | `None` |
| `my_dict.get("key", default)` | Returns default if key not found             | `my_dict.get("gender", "NA")` | `NA`   |

```python
print(my_dict["name"])
print(my_dict.get("name"))
print(my_dict.get("gender"))
print(my_dict.get("gender", "NA"))
```

---

## 🔁 2. Iterating Through a Dictionary

### 🟢 By Keys

```python
for key in my_dict:
    print(key)
```

### 🟢 By Key–Value Pairs

```python
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

### 🟢 Using `zip()` to combine keys and values

```python
for key, value in zip(my_dict.keys(), my_dict.values()):
    print(f"{key}: {value}")
```

### 🟢 Using `enumerate()` to show position

```python
for index, (key, value) in enumerate(my_dict.items(), start=1):
    print(f"{index} = {key}: {value}")
```

---

## ⚙️ 3. Dictionary Methods and Operations

| Method                  | Description                                    | Example                               |
| ----------------------- | ---------------------------------------------- | ------------------------------------- |
| `my_dict.keys()`        | Returns all keys                               | `dict_keys(['name', 'age', ...])`     |
| `my_dict.values()`      | Returns all values                             | `dict_values(['asit', 22, ...])`      |
| `my_dict.items()`       | Returns key–value pairs                        | `dict_items([('name', 'asit'), ...])` |
| `my_dict.update({...})` | Adds or updates keys                           | `my_dict.update({"gender": "male"})`  |
| `my_dict.pop(key)`      | Removes and returns a key’s value              | `my_dict.pop("name")`                 |
| `my_dict.popitem()`     | Removes and returns the **last inserted** item | `('full_name', 'shankar')`            |
| `key in my_dict`        | Checks if key exists                           | `if "gender" in my_dict:`             |
| `my_dict.copy()`        | Returns a shallow copy                         | `dict_copy = my_dict.copy()`          |

---

### 🧪 Example

```python
my_dict["gender"] = "female"
my_dict.update({"gender": "male"})  # overwrites if exists

dict_copy = my_dict.copy()
dict_copy["name"] = "shankar"

dict_copy["full_name"] = dict_copy.pop("name")
last_item = dict_copy.popitem()
```

**Output Example:**

```
my_dict after gender addition {'name': 'asit', 'age': 22, 'salary': 100.5, 'has_6_pack_abs': False, 'gender': 'male'}
{'name': 'asit', 'age': 22, 'salary': 100.5, 'has_6_pack_abs': False, 'gender': 'male'}
{'age': 22, 'salary': 100.5, 'has_6_pack_abs': False, 'gender': 'male', 'full_name': 'shankar'}
('full_name', 'shankar')
```

---

## 🧍‍♂️ 4. Copying and Mutability

When you use:

```python
dict_copy = my_dict.copy()
```

It creates a **shallow copy** — a new dictionary object,
but if any values are mutable (like lists), both copies would reference the same inner object.

Use `copy.deepcopy()` when you want to **fully clone** nested dictionaries.

---

## 🧮 5. Checking for Key Existence

```python
if "gender" in my_dict:
    print("gender key is available in dict")
```

Output:

```
gender key is available in dict
```

---

## 🧠 Key Takeaways

* Dictionaries are **unordered, mutable mappings** of unique keys to values.
* `.get()` is safer than `[]` access to avoid `KeyError`.
* `.update()` can **add** or **modify** multiple keys at once.
* `.popitem()` removes the **last inserted** key-value pair.
* Use `.copy()` or `copy.deepcopy()` depending on how deep you want to clone.

---

## ▶️ How to Run

1. Save the file as `dict_operations.py`
2. Open a terminal in the same folder.
3. Run:

```bash
python3 dict_operations.py
```

---

## 📚 References

* [Python Dictionary Docs](https://docs.python.org/3/library/stdtypes.html#dict)
* [copy module — shallow vs deep copy](https://docs.python.org/3/library/copy.html)
* [PEP 468 — Preserving Key Order](https://peps.python.org/pep-0468/)




