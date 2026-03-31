# # "Data una lista di studenti, ognuno con un nome e un voto, trovare il nome dello studente con il voto più alto."

# # # Come sono strutturati i dati?
# # Student = dict[str, str | float]
# # Students = list[Student]

# students = [
#     {"name": "Alice", "grade": 6.5},
#     {"name": "Bob", "grade": 9.2},
#     {"name": "Charlie", "grade": 7.8},
#     {"name": "David", "grade": 9.5},
#     {"name": "Eve", "grade": 8.8}
# ]

# # Approccio Top-Down
# # 1. Trova il voto più alto
# max_grade: float = 0.0
# for student in students: # {"name": "Alice", "grade": 6.5}
#     if student["grade"] > max_grade: # 6.5 > 0.0
#         max_grade = student["grade"] # max_grade = 6.5
# print(f"Il voto più alto è {max_grade}") # Il voto più alto è 9.5
# # Trova il nome dello studente con il voto più alto
# top_student: str = ""
# for student in students: # {"name": "Alice", "grade": 6.5}
#     if student["grade"] == max_grade: # 6.5 == 9.5
#         top_student = student["name"] # top_student = "Alice"
# print(f"Lo studente con il voto più alto è {top_student}") # Lo studente con il voto più alto è David


# ciclo diretto sulla lista
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# ciclo su una stringa
for x in "banana": # lista di caratteri
  print(x)

# ciclo su un indice (range)
for x in range(6): # range(6) -> [0, 1, 2, 3, 4, 5]
  print(x)

# range con inizio e fine
for x in range(2, 6): # range(2, 6) -> [2, 3, 4, 5]
  print(x)

# range con inizio, fine e passo
for x in range(2, 10, 3): # range(2, 10, 3) -> [2, 5, 8]
  print(x)


# append()	Adds an element at the end of the list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# sort()	Sorts the list

# Example of usage of append()
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits) # ['apple', 'banana', 'cherry', 'orange']
# Example of usage of index()
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana")) # 1
# Example of usage of insert()
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits) # ['apple', 'orange', 'banana', 'cherry']
# Example of usage of pop()
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits) # ['apple', 'cherry']
# Example of usage of remove()
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits) # ['apple', 'cherry']
# Example of usage of sort()
fruits = ["banana", "cherry", "apple"]
fruits.sort()
print(fruits) # ['apple', 'banana', 'cherry']
# sort() con reverse=True
fruits = ["banana", "cherry", "apple"]
fruits.sort(reverse=True)
print(fruits) # ['cherry', 'banana', 'apple']
# sort() con key ultimo carattere
fruits = ["banana", "cherry", "apple"]
fruits.sort(key=lambda x: x[-1])
print(fruits) # ['banana', 'apple', 'cherry']
# stessa cosa con def per la key
def last_char(s: str) -> str:
    return s[-1]
fruits = ["banana", "cherry", "apple"]
fruits.sort(key=last_char)
print(fruits) # ['banana', 'apple', 'cherry']


# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

# Example of usage of get()
student = {"name": "Alice", "grade": 6.5}
print(student.get("name")) # Alice
print(student["name"]) # Alice
print(student["age"]) # KeyError: 'age'
print(student.get("age", 18)) # 18 (default value)
# Example of usage of update()
student = {"name": "Alice", "grade": 6.5}
student.update({"grade": 7.0})
student["grade"] = 7.0
# Example of usage of items()
# Example of usage of keys()
# Example of usage of values()
# Example using a for loop to iterate over the 3 methods above
student = {"name": "Alice", "grade": 6.5}
for key in student.keys():
    print(key) # name, grade
for value in student.values():
    print(value) # Alice, 6.5
for key, value in student.items():
    print(f"{key}: {value}") # name: Alice, grade: 6.5

# funzione per verificare se un numero e' pari o dispari
def is_even(n: int) -> bool: # n = 4
    if n % 2 == 0: # 4 % 2 == 0 -> True, 5 % 2 == 0 -> False
        return True # numero pari
    else:
        return False # numero dispari

result: bool = is_even(4)
print("Il numero 4 è pari?", result) # Il numero 4 è pari? True



# funzione per verificare un numero e' divisibile per 3 e per 5

# numeri divisibili per 3 e per 5: 0, 15, 30, 45, 60, ...
# 9 --> 9 % 3 == 0 -> True, 9 % 5 == 4 -> False
# 15 --> 15 % 3 == 0 -> True, 15 % 5 == 0 -> True

def is_divisible_by_3_and_5(n: int) -> bool: # n = 15
    if n % 3 == 0 and n % 5 == 0: # 15 % 3 == 0 -> True, 15 % 5 == 0 -> True
        return True # numero divisibile per 3 e per 5
    else:
        return False # numero non divisibile per 3 e per 5