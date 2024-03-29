from typing import Optional

class Mother:
    def __init__(self, name: str):
        self.name: str = name
        self.children: list['Child']  = [] # list of Child objects

    def add_child(self, child: 'Child'):
        self.children.append(child) # reference from Mother to Child
        child.set_mother(self) # reference from Child to Mother

class Child:
    def __init__(self, name: str):
        self.name: str = name
        self.mother: Optional['Mother'] = None # Optional Mother object
    
    def set_mother(self, mother: 'Mother'): # Optional
        self.mother = mother

# Example of usage
mother = Mother("Jane")
child1 = Child("Alice")
child2 = Child("Bob")

mother.add_child(child1)
mother.add_child(child2)

print(mother.name, "has children:", [child.name for child in mother.children])
print(child1.name, "has mother:", child1.mother.name) # type: ignore