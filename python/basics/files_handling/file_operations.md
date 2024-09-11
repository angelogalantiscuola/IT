# File Operations in Python

## Example File

Let's start with an example file named `example.txt` with the following content:

```
This is the first line.
This is the second line.
This is the third line.
```

## Reading a File

To read a file in Python, you can use the `open()` function with the mode `'r'` for reading. Here is an example:

```python
# Open a file for reading
with open('example.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()
    print(content)
```

## Reading a File Line by Line

To read a file line by line in Python, you can use a loop to iterate over the file object. Here is an example:

```python
# Open a file for reading
with open('example.txt', 'r') as file:
    # Read the file line by line
    for line in file:
        print(line.strip())
```

**Output:**
```
Hello, world!
Appended text.
```

**Output:**
```
This is the first line.
This is the second line.
This is the third line.
```

## Writing to a File

To write to a file in Python, you can use the `open()` function with the mode `'w'` for writing. Here is an example:

```python
# Open a file for writing
with open('example.txt', 'w') as file:
    # Write some content to the file
    file.write('Hello, world!')
```

**Content of `example.txt` after writing:**
```
Hello, world!
```

## Appending to a File

To append to a file in Python, you can use the `open()` function with the mode `'a'` for appending. Here is an example:

```python
# Open a file for appending
with open('example.txt', 'a') as file:
    # Append some content to the file
    file.write('\nAppended text.')
```

**Content of `example.txt` after appending:**
```
Hello, world!
Appended text.
```

