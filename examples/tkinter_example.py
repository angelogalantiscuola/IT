# IMPORTANT: do not run it in SSH, it will not work
# run it in your local machine
import tkinter as tk


def say_hello():
    print("Hello, World!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="Say Hello", 
                   fg="red",
                   command=say_hello)
button.pack(side=tk.LEFT)

quit_button = tk.Button(frame,
                        text="QUIT", 
                        fg="blue",
                        command=root.quit)
quit_button.pack(side=tk.LEFT)

root.mainloop()