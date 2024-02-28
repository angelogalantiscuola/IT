# Multiple inheritance

In general, multiple inheritance should be used judiciously as it can lead to complex inheritance structures.

```python
class Bird:
    def fly(self):
        return "I can fly"

class Horse:
    def run(self):
        return "I can run"

class Pegasus(Bird, Horse):
    def magic(self):
        return "I'm a magical creature"

# Create an instance of Pegasus
pegasus = Pegasus()

# Call methods
print(pegasus.fly())  # Outputs: I can fly
print(pegasus.run())  # Outputs: I can run
print(pegasus.magic())  # Outputs: I'm a magical creature
```
