# OOP

## Syntax

```python
class User:
    # class attributes
    user_count = 0
    ALLOWED_PET = ['dog', 'cat', 'fish', 'rat']

    def __init__(self, first, last, age, pet):
        if pet not in User.ALLOWED_PET:
            raise ValueError(f"You can't have a {pet} pet!")

        # instance attributes
        self.first = first
        self.last = last
        self.age = age
        self.pet = pet

        User.user_count += 1

    # instance methods
    def full_name(self):
        return f"{self.first} {self.last}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def birthday(self):
        self.age += 1

    # class methods
    @classmethod
    def display_active_users(cls):
        return cls.user_count

    @classmethod
    def from_string(cls, data_str):
        first, last, age, pet = data_str.split(",")
        return cls(first, last, age, pet)
```

## Conventions

- `_name`: A single leading underscore in front of a variable, a function, or a method name means that these objects are used internally. This is more of a syntax hint to the programmer and is not enforced by the Python interpreter which means that these objects can still be accessed in one way on another from another script.
- `__name`: Python interpreter uses the double underscore to avoid naming conflict in Python subclasses. It uses the double underscore to rewrite the attribute name in Python classes. The rewriting of the attribute name in order to avoid collision is called name mangling.
- `__name__`: Dunder methods are methods that allow instances of a class to interact with the built-in functions and operators of the language.

## Inheritance

### Inheritance Syntax

```python
class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy
```

## Properties

### Property basic syntax

Python’s `property()` is the Pythonic way to avoid formal getter and setter methods in your code. This function allows you to turn class attributes into properties or managed attributes. Since `property()` is a built-in function, you can use it without importing anything. Additionally, `property()` was implemented in C to ensure optimal performance.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )
```

### Property using decorators

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius
```

## MRO (Method Resolution Order)

Whenever you create a class, Python sets a method resolution order, or MRO, for that class, which is the order in which Python will look for methods on instances of that class.

You can programmatically reference the MRO three ways:

- `__mro__` attribute on the class
- use the `mro()` method on the class
- user the builtin `help(cls)` method
