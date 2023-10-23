# Debugging

## Common errors

- SyntaxError
  - Occurs when python encounters incorrect syntax
- NameError
  - Occurs when a variable is not defined, i.e. is hasn't been assigned
- TypeError
  - An operation or function is applied to the wrong type
- IndexError
  - Occurs when you try to access an element in a list using an invalid index(i.e. one that is outside the range of the list or string)
- ValueError
  - This occurs when a built-in operation or function receives an argument that has the right type but an inappropriate value
- KeyError
  - Occurs whan a dictionary does not have a specific key
- AttributeError
  - Occurs when a variable does not have an attribute

## Raising errors

In python, we can throw errors using the `raise` keyword. Like so:

```python
raise ValueError('invalid value')
```

## Handling errors

```python
"""
catch all example
"""
try:
  # block of code
except:
  # do something

"""
catching specific errors
"""
try:
  # block of code
except NameError as err:
  # do something if NameError with err

"""
complete syntax
"""
try:
    # block of code
except NameError as err:
    # do something if NameError with err
except TypeError as err:
    # do something if TypeError with err
except (KeyError, AttributeError) as err:
    # do something if KeyError or AttributeError with err
except:
    # do something if any error
else:
    # code that runs if nothing was raised
finally:
    # code that runs no matter what

"""
example
"""
while True:
    try:
        num = int(input("please enter a number: "))
    except:
        print("That's not a number!")
    else:
        print("Good job, you entered a number!")
        break
    finally:
        print("Developed by Raphael")
```

## Debugger

[Docs](https://docs.python.org/3/library/pdb.html)

```python
"""
importing
"""
import pdb;  pdb.set_trace()

"""
use case
"""
first = "First"
second = "Second"
result = first + second
import pdb;  pdb.set_trace()
third = "Third"
result += third
print(result)

"""
common commands
"""

# l (list)
# n (next line)
# p (print)
# c (continue - finished debugging)
```
