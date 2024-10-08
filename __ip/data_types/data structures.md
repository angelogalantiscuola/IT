# Data structures

```toc
```

## How to choose which data structure to use?

The choice of data structure depends on the specific requirements of your program. Here are some general guidelines:

- Use arrays when you need constant-time access to elements and don't need to insert or delete elements frequently.
- Use lists when you need to insert or delete elements frequently, or when you don't know the size of the data in advance.
- Use maps when you need to associate keys with values and perform lookups based on keys.
- Use stacks when you need to implement a last-in, first-out (LIFO) data structure.
- Use queues when you need to implement a first-in, first-out (FIFO) data structure.
- Use trees when you need to store hierarchical data and perform operations such as searching, insertion, and deletion efficiently.
- Use graphs when you need to represent complex relationships between objects.

## Data structures description
### Array

An array is a data structure that **stores a collection of elements of the same type in a contiguous block of memory.** The elements in an array are accessed using an index, which is an integer value that represents the position of an element in the array. Arrays are commonly used in programming to store and manipulate collections of data, such as a list of numbers or a set of strings.

- C#: `System.Array`
- Java: `java.util.Arrays`
- Python: `list` or `array` (from the `array` module)
- JavaScript: `Array`

```python
import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Access elements
print(arr[0])  # Output: 1
```

### List

A list is a data structure that consists of a sequence of nodes, where each node contains a value and a reference to the next node in the sequence. **Unlike arrays, linked lists do not store their elements in contiguous memory locations.** Instead, each node in a linked list points to the next node, forming a chain-like structure. Linked lists can be used to implement various abstract data types, such as stacks, queues, and associative arrays.

- C#: `System.Collections.Generic.List<T>`
- Java: `java.util.List<E>`
- Python: `list`
- JavaScript: `Array` (although it behaves more like a dynamic array than a traditional linked list)

```python
# Create a list of integers
lst = [1, 2, 3, 4, 5]

# Access elements
print(lst[0])  # Output: 1

# Append an element
lst.append(6)

# Remove an element
lst.remove(3)
```

### Map

 A map is a data structure that stores **key-value pairs**, where each key is unique. **It is also known as a dictionary, associative array, or hash table** in different programming languages. The map allows for efficient lookup, insertion, and deletion of key-value pairs. The keys are used to index and locate the corresponding values. Maps are commonly used in various applications such as databases, caching, and indexing.

- C#: `System.Collections.Generic.Dictionary<TKey, TValue>`
- Java: `java.util.Map<K, V>`
- Python: `dict`
- JavaScript: `Map`

```python
# Create a dictionary
dct = {'a': 1, 'b': 2, 'c': 3}

# Access elements
print(dct['a'])  # Output: 1

# Add a new key-value pair
dct['d'] = 4

# Remove a key-value pair
del dct['b']
```

### Set

 A set is an abstract data type that represents a collection of distinct elements. **The elements in a set are unordered**, meaning that there is no concept of a "first" or "last" element. Sets are often used to represent mathematical sets, which are collections of unique elements.

- C#: `System.Collections.Generic.HashSet<T>`
- Java: `java.util.Set<E>`
- Python: `set`
- JavaScript: `Set`

```python
# Create a set
st = {1, 2, 3, 4, 5}

# Add an element
st.add(6)

# Remove an element
st.remove(3)

# Check if an element is in the set
print(4 in st)  # Output: True
```

### Stack

A stack is a data structure that stores a **collection of elements and operates on them in a last-in, first-out (LIFO)** manner. Elements can be added to the top of the stack, and removed from the top of the stack. This means that the last element added to the stack is the first one to be removed. Stacks can be used to implement various algorithms, such as depth-first search and backtracking. They are also used in programming languages to manage function calls and local variables.

- C#: `System.Collections.Generic.Stack<T>`
- Java: `java.util.Stack<E>`
- Python: `list` (although it can be used as a stack by using the `append()` and `pop()` methods)
- JavaScript: There is no built-in Stack data structure in JavaScript, but you can implement a Stack using an Array.

```python
# Create a stack using a list
stack = []

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Pop elements from the stack
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
```

### Queue

A queue is a data structure that stores a **collection of elements and operates on them in a first-in, first-out (FIFO)** manner. Elements can be added to the back of the queue, and removed from the front of the queue. This means that the first element added to the queue is the first one to be removed. Queues can be used to implement various algorithms, such as breadth-first search and job scheduling. They are also used in computer systems to manage tasks and requests.

- C#: `System.Collections.Generic.Queue<T>`
- Java: `java.util.Queue<E>`
- Python: `queue.Queue`
- JavaScript: There is no built-in Queue data structure in JavaScript, but you can implement a Queue using an Array or a LinkedList.

```python
from queue import Queue

# Create a queue
q = Queue()

# Enqueue elements
q.put(1)
q.put(2)
q.put(3)

# Dequeue elements
print(q.get())  # Output: 1
print(q.get())  # Output: 2
```

### Tree

A tree is a data structure that consists of a **collection of nodes, where each node has a value and zero or more child nodes**. The topmost node in a tree is called the root, and each child node is connected to its parent node by a single edge. Trees are commonly used in computer science to represent hierarchical structures, such as file systems, organization charts, and HTML documents. They can also be used to implement various algorithms, such as binary search and decision trees.

- C#: There is no built-in Tree data structure in C#, but you can implement a Tree using classes and objects.
- Java: `java.util.TreeMap<K, V>` (for a binary search tree) and `java.util.TreeSet<E>` (for a binary search tree that stores only keys)
- Python: There is no built-in Tree data structure in Python, but you can implement a Tree using classes and objects.
- JavaScript: There is no built-in Tree data structure in JavaScript, but you can implement a Tree using classes and objects.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

# Create a tree
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
root.children.append(child1)
root.children.append(child2)

# Access elements
print(root.value)  # Output: 1
print(root.children[0].value)  # Output: 2
```

### Graph

A graph is a data structure that consists of a **collection of nodes, called vertices, and a collection of edges that connect pairs of vertices**. Each edge can be directed or undirected, and can have a weight or a cost associated with it. Graphs are commonly used in computer science to represent complex relationships between objects, such as social networks, road networks, and computer networks. They can also be used to implement various algorithms, such as shortest path algorithms and minimum spanning tree algorithms.

- C#: There is no built-in Graph data structure in C#, but you can implement a Graph using classes and objects.
- Java: `org.jgrapht.Graph<V, E>`
- Python: `networkx.Graph`
- JavaScript: There is no built-in Graph data structure in JavaScript, but you can implement a Graph using classes and objects.

```python
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes
G.add_node(1)
G.add_node(2)

# Add an edge
G.add_edge(1, 2)

# Access nodes and edges
print(G.nodes)  # Output: [1, 2]
print(G.edges)  # Output: [(1, 2)]
```

## Programming languages data structures

Most programming languages have several common data structures, such as

- arrays,
- lists,
- map,
- set,
- stacks,
- queues,
- trees,
- graphs.

```python
### Array
+---+---+---+---+---+
| 1 | 2 | 3 | 4 | 5 |
+---+---+---+---+---+

### List
1 -> 2 -> 3 -> 4 -> 5

### Map (Dictionary)
a: 1
b: 2
c: 3
d: 4

### Set
{ 1, 2, 3, 4, 5 }

### Stack
| 3 |
| 2 |
| 1 |
+---+

### Queue
1 <- 2 <- 3

### Tree
    1
   / \
  2   3
 / \
4   5

### Graph
  1
 / \
2 - 3
 \ /
  4
  
```