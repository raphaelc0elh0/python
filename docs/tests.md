# Tests

## Why?

- Reduce bugs in exisiting code
- Ensure bugs that are fixed and stay fixed
- Ensure that new feature don't break old ones
- Ensure that cleaning up code doesn't introduce new bugs

## Assertions

- We can make simple assertions with the `assert` keyword
- `assert` expects an expression
- Returns `None` if the experssion is truthy
- Raises an `AssertionError` if the expression is falsy
- Accepts an optional error message as second argument

```python
def add_positive_numbers(x, y):
  assert x > 0 and y > 0, "Both numbers must be positive!"
  return x + y
```

## Doctests

- We can write teste for functions inside of the docstring
- Write code that looks like it's inside of a REPL

```python
"""
This is the "example" module.
The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""
```

Cons:

- Syntax is a little strange
- Clutters up our function code
- Lacks many features of larger testing tools
- Tests can be brittle

## unittest

- Python comes with a built-in module called `unittest`
- You can write unit tests encapsulated as classes that inherit from `unittest.TestCase`
- This inheritance gives you access to many assertion helpers that let you test behaviour of our functions
- You can run tests by calling `unittest.main()`

[Docs Reference](https://docs.python.org/3/library/unittest.html)

```python
"""
example
"""
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

"""
example with comments
"""
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
```

To see comments, it should run by: `python <name_of_the_file> -v`

### Types of assertions

- `self.assertEqual()`
- `self.assertNotEqual()`
- `self.assertTrue()`
- `self.assertFalse()`
- `self.assertIsNone()`
- `self.assertIsNotNone()`
- `self.assertIn()`
- `self.assertNotIn()`

### Testing for errors

```python
class SomeTests(unittest.TestCase):

  def testing_for_error(self):
    """testing for an error"""
    with self.assertRaises(IndexError):
      l = [1, 2, 3]
      l[100]
```

### Before and after hooks

- `setUp` and `tearDown`
- `setUp` runs before each test method
- `tearDown` runs after each test method
- Common use cases: adding/removing data from a test database, creating instances of a class

```python
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
```
