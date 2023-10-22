# Basics

## Variables

### Restrictions

1. Variables must start with a letter or underscore
2. The rest od the name must consist of letters, numbers ou underscores
3. Names are case-sensitive

### Conventions

- Most variables should be **snake_case**
- Most variables should be **lowercase**, with some exceptions
  - **CAPITAL_SNAKE_CASE** usually refers to constants
  - **UpperCamelCase** usually refers to a class
- **\_\_dunder\_\_** are supposed to be private or left alone

## Loops

### `for` loop

```python
ages = range(10) # https://docs.python.org/3/library/stdtypes.html#range
for age in ages:
    print(age)
```

### `while` loop

```python
user_response = None
while user_response != "please":
  user_response = input("Ah ah ah, you didn't say the magic word: ")
```

> `break` keyword
>
> `break` allows you to exit a loop when an external condition is met

## Comments

```python
  # This is a comment
  # with multiple lines

  """
    This is a comment
    with multiple lines
  """

  print(type(2/1)) # this is a inline comment

  def is_palindrome(word):
    """Check if word is a palindrome. This is a doc string."""
    str(word) == str(word)[::-1]
```

## Built-in Types

### Strings

```python
"""
basic declaration
"""
string = "this is a string"

"""
concatenation
"""
concatenated = "this" + "is" + "a" + "string"

"""
formatting
"""
x = 10
formatted = f"I've told you {x} times already!"
print(formatted) # I've told you 10 times already!

"""
indexed
"""
var = "stupid"
print(var[0]) # s
print(var[len(var) - 1]) # d
```

### Numbers and Operators

- int: Integer number
- float: Floating point number
- complex: Complex number

#### Operators

| Symbol | Name             |
| ------ | ---------------- |
| +      | Addition         |
| -      | Subtraction      |
| \*     | Multiplication   |
| /      | Division         |
| \*\*   | Exponentiation   |
| %      | Modulo           |
| //     | Integer division |

> division always returns float

### Booleans and Conditional Logic

```python
"""
if statements
"""
if name == "Arya Stark":
  print("Valar Morghulis")
elif name == "Jon Snow":
  print("You know nothing")
else:
  print("Carry on")

```

#### Comparison operators

| Symbol | Name                     |
| ------ | ------------------------ |
| ==     | Same value               |
| !=     | Not same value           |
| >      | Greater than             |
| <      | Less than                |
| <=     | Greater than or equal to |
| >=     | Less than or equal to    |

> `is` and `is not` operators
>
> The `is` keyword is used to test if two variables refer to the same object.
> The test returns `True` if the two objects are the same object.
> The test returns `False` if they are not the same object, even if the two objects are 100% equal. Use the == operator to test if two variables are equal.

#### Logical operators

| Symbol | Name                |
| ------ | ------------------- |
| and    | Logical conjunction |
| or     | Logical disjuction  |
| not    | Logical negation    |

#### Truthy and falsy values

- Truthy
  - Non-empty sequences or collections (lists, tuples, strings, dictionaries, sets).
  - Numeric values that are not zero.
  - `True`
- Falsy
  - Sequences and collections
    - Empty lists: `[]`
    - Empty tuples: `()`
    - Empty dictionaries: `{}`
    - Empty sets: `set()`
    - Empty strings: `""`
    - Empty ranges: `range(0)`
  - Numbers
    - Zero of any numeric type
    - Integer: `0`
    - Float: `0.0`
    - Complex: `0j`
  - Constants
    - `None`
    - `False`

## Built-in Data Structures

### Lists

```python
tasks = ["Install python", "Learn python", "Take a break"]
print(tasks[1]) # "Learn python"
```

#### Slicing

Makes a new list using slices of the old list: `some_list[start:end:step]`

```python
tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tasks[0:1])  # [1]
print(tasks[5:8])  # [6, 7, 8]
print(tasks[2:7:2])  # [3, 5, 7]
print(tasks[2::2])  # [3, 5, 7, 9]
print(tasks[::2])  # [1, 3, 5, 7, 9]
```

#### List Methods

```python
"""
  append: add an item to the end of the list
"""
first_list = [1,2,3,4]
first_list.append(5)
print(first_list) # [1,2,3,4,5]

"""
  extend: add to the end of a list all values passed to extend
"""
first_list = [1,2,3,4]
first_list.append([5,6,7,8])
print(first_list) # [1,2,3,4,[5,6,7,8]]
correct_list = [1,2,3,4]
correct_list.extend([5,6,7,8])
print(correct_list) # [1,2,3,4,5,6,7,8]

"""
  insert: insert and item at a given position
"""
first_list = [1, 2, 3, 4]
first_list.insert(1, 0)
print(first_list)  # [1,0,2,3,4]
first_list.insert(3, 0)
print(first_list)  # [1,0,2,0,3,4]
first_list.insert(-1, 0)
print(first_list)  # [1,0,2,0,3,0,4]
first_list.insert(len(first_list), 0)
print(first_list)  # [1,0,2,0,3,0,4,0]

"""
  clear: remove all items from the list
"""
first_list = [1, 2, 3, 4]
first_list.clear()
print(first_list)  # []

"""
  pop: remove the item at the given position (if none, last item) and return it
"""
first_list = [1, 2, 3, 4]
first_list.pop()
print(first_list)  # [1,2,3]
first_list.pop(0)
print(first_list)  # [2,3]

"""
  remove: remove the first item from the list whose value is x. Throws if not found
"""
first_list = [1, 2, 3, 4]
first_list.remove(4)
print(first_list)  # [1,2,3]
first_list.remove(0)
print(first_list)  # ValueError: list.remove(x): x not in list
```

#### List comprehension (LC)

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

```python
  # Syntax
  [___ for ___ in ___ ]
```

Without LC:

```python
nums = [1, 2, 3]
multiplied = []
for x in nums:
    multiplied.append(x*10)
print(multiplied)  # [10, 20, 30]
```

With LC:

```python
nums = [1, 2, 3]
multiplied = [x*10 for x in nums]
print(multiplied)  # [10, 20, 30]
```

With LC with conditional logic:

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = [x for x in nums if x % 2 == 0]
print(evens)  # [2, 4, 6, 8]
odds = [x for x in nums if x % 2 == 1]
print(odds)  # [1, 3, 5, 7, 9]
```

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [x*2 if x % 2 == 0 else x/2 for x in nums]
print(result)  # [0.5, 4, 1.5, 8, 2.5, 12, 3.5, 16, 4.5]
```

```python
with_vowels = "This is so much fun!"
without_vowels = ''.join(char for char in with_vowels if char not in "aeiou")
print(without_vowels)  # Ths s s mch fn!
```

### Dictionaries

Dictionaries are used to store data values in key:value pairs.

```python
me = {
    "name": "Raphael",
    "owns_dog": True,
    "num_of_dogs": 3,
    "favorite_language": "Python",
    "is_funny": False,
    0: "Interesting key!",
}

print(me["name"])  # "Raphael"
print(me["num_of_dogs"])  # 3
print(me["is_funny"])  # False

"""
using dict() function
"""
me_dict = dict(
    name="Raphael",
    owns_dog=True,
    num_of_dogs=3,
    favorite_language="Python",
    is_funny=False,
) # this syntax does not allow integer keys

me_dict_another_syntax = dict([
    ("name", "Raphael"),
    ("owns_dog", True),
    ("num_of_dogs", 3),
    ("favorite_language", "Python"),
    ("is_funny", False),
    (0, "Interesting key!"),
])
```

#### Iterating through dictionaries

```python
me = {
    "name": "Raphael",
    "owns_dog": True,
    "num_of_dogs": 3,
    "favorite_language": "Python",
    "is_funny": False,
    0: "Interesting key!",
}

for key in me:
    print(key)
"""
name
owns_dog
num_of_dogs
favorite_language
is_funny
0
"""

for key in me.keys():
    print(key)
"""
name
owns_dog
num_of_dogs
favorite_language
is_funny
0
"""

for value in me.values():
    print(value)
"""
Raphael
True
3
Python
False
Interesting key!
"""

for (key, value) in me.items():
    print(f"{key}: {value}")
"""
name: Raphael
owns_dog: True
num_of_dogs: 3
favorite_language: Python
is_funny: False
0: Interesting key!
"""
```

#### Dictionary methods

```python
me = {
    "name": "Raphael",
    "owns_dog": True,
    "num_of_dogs": 3,
    "favorite_language": "Python",
    "is_funny": False,
    0: "Interesting key!",
}

"""
clear: clears a dictionary
"""
me.clear()
print(me)  # {}

"""
copy: makes a copy of a dicitionary
"""
you = me.copy()
print(you)  # {'name': 'Raphael', 'owns_dog': True, 'num_of_dogs': 3, 'favorite_language': 'Python', 'is_funny': False, 0: 'Interesting key!'}
you is me # False
you == me # True

"""
fromkeys: creates key-value pairs from comma separated values
"""
print({}.fromkeys("a", "b"))  # {'a': 'b'}
print({}.fromkeys(["email"], "unknown"))  # {'email': 'unknown'}
print({}.fromkeys("a", [1, 2, 3, 4, 5]))  # {'a': [1, 2, 3, 4, 5]}

"""
get: retrieves a key in an object and return None instead of a KeyError if it does not exist
"""
d = dict(a=1, b=2, c=3)
print(d["a"])  # 1
print(d.get("a"))  # 1
print(d["no_key"])  # KeyError: 'no_key'
print(d.get("no_key"))  # None

"""
pop: takes a single argument corresponding to a key and removes that key-value pair from the dictionary. Returns de value corresponding to the key that was removed
"""
d = dict(a=1, b=2, c=3)
removed = d.pop("a")
print(d)  # {'b': 2, 'c': 3}
print(removed)  # 1
print(e)  # NameError: name 'e' is not defined

"""
popitem: removes a rendom key in a dictionary
"""
d = dict(a=1, b=2, c=3)
removed = d.popitem()
print(d)  # {'a': 1, 'b': 2}
print(removed)  # ('c', 3)

"""
update: update keys and values in a dictionary with another sert of key value pairs
"""
first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}

second.update(first)
print(second)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

second["a"] = "AMAZING"
print(second)  # {'a': 'AMAZING', 'b': 2, 'c': 3, 'd': 4, 'e': 5}

second.update(first)
print(second)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

#### Dictionary comprehension (DC)

Like List Comprehension, Python allows dictionary comprehensions. We can create dictionaries using simple expressions.

```python
  # Syntax
  { ___:___ for ___ in ___ }
```

Examples:

```python
numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)  # {'first': 1, 'second': 4, 'third': 9}
```

```python
dictionary = {num: num**2 for num in [1, 2, 3, 4, 5]}
print(dictionary)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```python
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)  # {'A': '1', 'B': '2', 'C': '3'}
```

With conditional logic:

```python
num_list = [1, 2, 3, 4]
result = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(result)  # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
```

```python
instructor = {'name': 'raphael', 'city': 'recife', 'color': 'purple'}
result = {(k.upper() if k is 'color' else k): v.upper() for k, v in instructor.items()}
print(result)  # {'name': 'RAPHAEL', 'city': 'RECIFE', 'COLOR': 'PURPLE'}
```

### Tuples

Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and **unchangeable**.

```python
x = (1, 2, 3)
print(3 in x)  # True
x[0] = "change, me!"  # TypeError: 'tuple' object does not support item assignment
```

```python
tuple_example = tuple([1, 2, 3, 4, 5])
print(tuple_example)  # (1, 2, 3, 4, 5)
```

```python
tuple_example = tuple([1, 2, 3, 4, 5])
print(tuple_example)  # (1, 2, 3, 4, 5)
print(tuple_example[1])  # 2
```

```python
locations = {
    (35.6895, 39.6913): "Tokyo office",
    (40.7128, 74.0060): "New York office",
    (37.7749, 122.4194): "San Francisco office",
}  # tuples can be used as keys, lists can't

locs = {[35, 39]: 'Tokyo office'}  # TypeError: unhashable type: 'list
```

#### Tuple methods

```python
"""
count: returns the number of times a value appears in a tuple
"""
x = (1, 2, 2, 3, 3, 3)
print(x.count(1))  # 1
print(x.count(2))  # 2
print(x.count(3))  # 3

"""
index: returns the index at which a value is found in a tuple
"""
x = (1, 2, 2, 3, 3, 3)
print(x.index(1))  # 1
print(x.index(5))  # ValueError: tuple.index(x): x not in tuple
print(x.index(3))  # 3 - only the first matching index is returned
```

> Why use tuples?
>
> - Tuples are faster than lists
> - It makes your code safer
> - Valid keys in a dictionary
> - Some methods return them to you (like dictionary.items())

### Sets

Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, **unchangeable\***, unindexed and do not have duplicate values.

```python
s = set({1, 2, 3, 4, 5, 5, 5})
print(s) # {1, 2, 3, 4, 5} - sets cannot have duplicates

# creating a new set
s = set({1, 2, 3, 4, 5})
s = set([1, 2, 3, 4, 5])
s = {1, 2, 3, 4, 5}

print(s[1])  # TypeError: 'set' object is not subscriptable
print(4 in s)  # True
print(8 in s)  # False
```

One of the most common use cases is to get unique values from a list:

```python
letters = ["L", "A", "S", "V", "E", "G", "A", "S"]
print(list(set(letters)))  # ['G', 'L', 'E', 'A', 'V', 'S']
```

#### Set methods

```python
"""
add: adds an element to a set. If the element is already in the set, the set doesn't change
"""
s = set([1, 2, 3])
s.add(4)
print(s)  # {1, 2, 3, 4}
s.add(1)
print(s)  # {1, 2, 3, 4}

"""
remove: removes a value from the set - returns a KeyError if the value is not found
"""
s = set([1, 2, 3])
s.remove(1)
print(s)  # {2, 3}
s.remove(4)
print(s)  # KeyError: 4
"""
discard: removes a value from the set - but it doesn't throw error if value is not found
"""
s = set([1, 2, 3])
s.discard(1)
print(s)  # {2, 3}
s.discard(4)
print(s)  # {2, 3}

"""
copy: creates a copy of the set
"""
s = set([1, 2, 3])
another_s = s.copy()
print(another_s)  # {1, 2, 3}
print(another_s == s)  # True
print(another_s is s)  # False

"""
clear: removes all contents of the set
"""
s = set([1, 2, 3])
s.clear()
print(s)  # set()
```

#### Math sets

```python
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

print(math_students | biology_students)
# Union set
# {'Matthew', 'Oliver', 'James', 'Helen', 'Charlotte', 'Prashant', 'Aparna', 'Mesut', 'Jane'}

print(math_students & biology_students)
# Intersection set
# {'Matthew', 'James'}
```

#### Set comprehesions (SC)

Like Dictionary Comprehension, Python allows set comprehensions. We can create sets using simple expressions.

```python
  # Syntax
  { ___ for ___ in ___ }
```

```python
s = {x**2 for x in range(10)}
print(s)  # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
```

```python
def has_all_vowels(string):
    return len({char for char in string if char in 'aeiou'}) == 5

print(has_all_vowels("hello"))  # False
print(has_all_vowels("sequoia"))  # True
```
