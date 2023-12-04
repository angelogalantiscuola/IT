"""
Temporary file to test out some code
"""
import math

dicto = {"key": "value", "key2": "value2", "key3": 1}
listo = [dicto]
print(listo)



# List of all the attributes and methods
print(dir(math))
print("\n")
# Filter out these special attributes
print([name for name in dir(math) if not name.startswith("__")])
print("\n")

# Get all attributes and methods
all_items = dir(math)

# Filter methods and attributes
methods = [
    item
    for item in all_items
    if callable(getattr(math, item)) and not item.startswith("__")
]
attributes = [
    item
    for item in all_items
    if not callable(getattr(math, item)) and not item.startswith("__")
]

print("Methods:", methods)
print("\n")
print("Attributes:", attributes)
print("\n")
