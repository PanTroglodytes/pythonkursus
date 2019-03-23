# Labels
import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Hello Tkinter!")
label.pack()

root.mainloop()


# Buttons
def write_slogan():
    print("Tkinter is easy to use!")


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button_quit = tk.Button(frame, text="quit", fg="red", command=quit)
button_quit.pack(side=tk.LEFT)
button_hello = tk.Button(frame, text="Hello", command=write_slogan)
button_hello.pack(side=tk.LEFT)

root.mainloop()