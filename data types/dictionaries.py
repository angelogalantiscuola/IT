# Step 1: Create a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Step 2: Add an item to the dictionary
my_dict["job"] = "Engineer"

# Step 3: Change an item in the dictionary
my_dict["city"] = "San Francisco"

# Step 4: Delete an item from the dictionary
del my_dict["age"]

# Step 5: Loop through the dictionary
# Print keys
for key in my_dict:
    print(key)

# Print values
for value in my_dict.values():
    print(value)

# Print items
for key, value in my_dict.items():
    print(key, value)