# Dictionary

## What is a dictionary in Python?

In Python, a dictionary is an **unordered collection of key-value pairs**, where each key is unique. It is also known as an associative array or a hash table.

## How do I create a dictionary in Python?

You can create a dictionary in Python by enclosing a comma-separated list of key-value pairs in curly braces {}. Here's an example:

``` python
my_dict = {"apple": 2, "banana": 3, "orange": 4}
```

This creates a dictionary with three key-value pairs, where the keys are "apple", "banana", and "orange", and the corresponding values are 2, 3, and 4, respectively.


## How do I access the values of a dictionary in Python?

You can access the values of a dictionary in Python by using the keys as the index. Here's an example:

``` python
my_dict = {"apple": 2, "banana": 3, "orange": 4}
print(my_dict["apple"])  # Output: 2
```

This code accesses the value associated with the key "apple" in the dictionary my_dict and prints it to the console.

## From dictionary to JSON file

You can convert a dictionary to JSON in Python by using the json.dumps() function. Here's an example:

``` python
import json

my_dict = {"apple": 2, "banana": 3, "orange": 4}
json_str = json.dumps(my_dict)

print(json_str)  # Output: {"apple": 2, "banana": 3, "orange": 4}

# write to file
with open("my_dict.json", "w") as f:
    f.write(json_str)

```

This code imports the json module, creates a dictionary my_dict, and then converts it to a JSON string using the json.dumps() function and then saves it to a file named "my_dict.json" using the json.dump() function. The with statement is used to automatically close the file after writing.

## From JSON file to dictionary

In Python, you can convert a JSON string to a dictionary using the json module. Here's an example:

``` python
import json

json_str = '{"apple": 2, "banana": 3, "orange": 4}'
my_dict = json.loads(json_str)

print(my_dict)  # Output: {"apple": 2, "banana": 3, "orange": 4}
```

This code imports the json module, creates a JSON string json_str, and then converts it to a dictionary using the json.loads() function. The resulting dictionary is then printed to the console.

In Python, you can load a JSON file into a dictionary using the json module. Here's an example:

``` python
import json

with open("my_dict.json", "r") as f:
    my_dict = json.load(f)

print(my_dict)
```

This code imports the json module, opens a file named "my_dict.json" in read mode using the open() function, and then loads the contents of the file into a dictionary using the json.load() function. The resulting dictionary is then printed to the console.