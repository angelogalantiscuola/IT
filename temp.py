"""
Temporary file to test out some code
"""

text = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
print(text)

cyphers = [str(i) for i in range(10)]
total_sum = 0

for line in text.split("\n"):
    if not line == "":
        number_found = False
        first_number = None
        last_number = None
        for char in line:
            if char in cyphers:
                if not number_found:
                    first_number = char
                    last_number = char
                    number_found = True
                else:
                    last_number = char
        print(f"First number: {first_number}, Last number: {last_number}")
        line_number = int(first_number + last_number)
        total_sum += line_number

print(f"Total sum: {total_sum}")
