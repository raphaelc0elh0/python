# Files

## Operations

### Reading files

- You can read a file with the `open` function
- `open` returns a file object to you
- You can read a file object with the `read` method

[open() Docs](https://docs.python.org/3/library/functions.html#open)

```python
  file = open("story.txt")
  print(file) # <_io.TextIOWrapper name='story.txt' mode='r' encoding='UTF-8'>
  print(file.read()) # "This is a file containing a story.""
  print(file.read()) # ""
```

#### Cursor movement

- Python reads files by using a cursor
- After a file is read, the cursor is at the end
- To move the cursor, use the `seek` method

```python
  file = open("story.txt")
  print(file) # <_io.TextIOWrapper name='story.txt' mode='r' encoding='UTF-8'>
  print(file.read()) # "This is a file containing a story.""
  print(file.read()) # ""
  file.seek(0)
  print(file.read()) # "This is a file containing a story.""
```

### Closing files

Opening a file consumes system resources. If you don't close the file properly, these resources might not be released until the Python interpreter exits, which can lead to resource leaks.

- You can close a file with the `close` method
- You can check if a file is closed with the `closed` attribute
- Once close, a file can't be read again

#### I/O using `with` statements

```python
with open("story.txt") as file:
    print(file.read())  # "This is a file containing a story.""
```

> ### `with` blocks
>
> The `with` statement is used to simplify resource management. It is commonly used for file handling, but it can also be used with other types of objects that support a context manager.
>
> ```python
> class MyContextManager:
>     def __enter__(self):
>         print("Entering the context")
>         return self  # Can return any object that should be used within the 'with' block
>
>     def __exit__(self, exc_type, exc_value, traceback):
>         print("Exiting the context")
>         # Any cleanup code can go here
>
> # Using the custom context manager
> with MyContextManager() as cm:
>     # Code inside the 'with' block
>     print("Inside the context")
> # '__exit__' method is automatically called outside the 'with' block
> ```

### Writing files

- You can also use `open` to write to a file
- Need to specify the `w` flag as the second argument
- If file does not exist, it will be created

```python
with open("story.txt", "w") as file:
    file.write("This is overwriting whats in the file\n")

with open("story.txt", "r") as file:
    print(file.read())  # "This is overwriting whats in the file"
```

## Modes for opening files

- `r`: Read a file (no writing) - this is the default
- `w`: Write to a file (overwrites, creates file)
- `a`: Append to a file (append to the end of a file)
- `r+`: Read and write to a file (writing based on cursor, overwrites, does not create file)
