import psutil

# Get the CPU usage percentage
cpu_usage = psutil.cpu_percent()
print(f"CPU usage: {cpu_usage}%")

# Get memory usage
memory = psutil.virtual_memory()
print(f"Memory: {memory}")
