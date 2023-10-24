# Modules

## Why use modules?

- Keep python files small
- Reuse code across multiple files by importing
- A module is just a python file

## Syntax

```python
"""
simple import
"""
import random

result = random.choice(['a', 'b', 'c', 'd', 'e'])
print(result) # b

"""
simple import with "as" keyword
"""
import random as r

result = r.choice(['a', 'b', 'c', 'd', 'e'])
print(result) # c

"""
importing only what is needed using "from" keywords
"""
from random import random as r

result = r.choice(['a', 'b', 'c', 'd', 'e'])
print(result) # b

"""
importing multiple
"""
from random import choice, randint

result = choice(['a', 'b', 'c', 'd', 'e'])
print(result)  # a
result = randint(1, 100)
print(result)  # 90

"""
importing everything from module
"""
from random import *

result = choice(['a', 'b', 'c', 'd', 'e'])
print(result) # b
```

## External modules

- `pip`: package management system for python
- As of 3.4, comes with python by default

[Python Package Index](https://pypi.org/)

```python
python3 -m pip install <name_of_package>
```

## `import` summmary

When you use `import`, python...

1. Tries to find the module (if it fail, throws an error)
2. Runs the code inside of the module being imported
3. Then runs the code inside of the main module

To avoid running code outside the main module, there is a "trick":

```python
# imports

# block of code

if __name__ == "__main__":
    # execute only this block of code
```
