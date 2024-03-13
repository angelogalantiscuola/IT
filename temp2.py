# import psutil

# # Get the CPU usage percentage
# cpu_usage = psutil.cpu_percent()
# print(f"CPU usage: {cpu_usage}%")

# # Get memory usage
# memory = psutil.virtual_memory()
# print(f"Memory: {memory}")

# import requests

# # Making a GET request
# response = requests.get("https://api.github.com")
# # response = requests.get("https://github.com")
# # response = requests.get("https://github.com/sdadsaddafafdsd")

# # Checking the status code of the request
# print(response.status_code)

# # Printing the content of the response
# print(type(response.text))
# data = response.json()
# print(data)
# print(type(data))
# print(data["current_user_url"])


import matplotlib.pyplot as plt

# max_points = 10
# # y = x^2
# x = [i for i in range(1, max_points)]
# y_parabolic = [i**2 for i in range(1, max_points)]
# # y = 2^x
# y_exponential = [2**i for i in range(1, max_points)]
# plt.plot(x, y_parabolic)
# plt.plot(x, y_exponential)

# plt.savefig("graph.png")

# show a bar chart
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
marks = [2, 3, 4, 5, 4]

plt.bar(students, marks)
plt.savefig("graph2.png")
