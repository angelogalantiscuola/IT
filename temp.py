import os  # unused import

x= 1+2  # bad spacing
unused_var = 5  # unused variable

if x == None:  # comparison to None
    print("hello")

try:
    y=1/0  # division by zero, bad spacing
except:  # bare except
    pass

# very long line to exceed typical max line length configured by many linters (E501) .................................................................................................................................
print("done"); x=x+1  # multiple statements per line, bad spacing