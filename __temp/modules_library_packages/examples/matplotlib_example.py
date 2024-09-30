import matplotlib.pyplot as plt

max_points = 10
# y = x^2
x = [i for i in range(1, max_points)]
y_parabolic = [i**2 for i in range(1, max_points)]
# y = 2^x
y_exponential = [2**i for i in range(1, max_points)]
plt.plot(x, y_parabolic)
plt.plot(x, y_exponential)

plt.savefig("graph.png")

plt.clf()

# show a bar chart
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
marks = [2, 3, 4, 5, 4]

plt.bar(students, marks)
plt.savefig("graph2.png")

plt.clf()


person_id = [1, 2, 3, 4, 5, 6]
heigth = [170, 175, 180, 185, 190, 195]
weight = [85, 90, 100, 75, 80, 95]

plt.scatter(person_id, heigth, s=weight)

plt.savefig("graph3.png")
