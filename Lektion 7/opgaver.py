# Opgave 1
import tkinter as tk


root = tk.Tk()
frame_1 = tk.Frame(root)
frame_1.pack()

label_1_text = "Hej, velkommen til mit program! \n\n\n"

label_1 = tk.Label(frame_1, text=label_1_text)
label_1.pack()

# Opgave 2
def change_text():
    label_1_text = entry_felt.get() + "\n\n\n"
    label_1.config(text=label_1_text)


button_quit = tk.Button(frame_1, text="QUIT", fg="red", command=quit)
button_change = tk.Button(frame_1, text="Change text", command=change_text)
button_quit.pack()
button_change.pack()

# Opgave 3
quote = "HAMLET: To be, or not to be--that is the question: " \
        "Whether 'tis nobler in the mind to suffer " \
        "The slings and arrows of outrageous fortune " \
        "Or to take arms against a sea of troubles " \
        "And by opposing end them. To die, to sleep-- " \
        "No more--and by a sleep to say we end " \
        "The heartache, and the thousand natural shocks " \
        "That flesh is heir to. 'Tis a consummation " \
        "Devoutly to be wished. "

tekst_felt = tk.Text(frame_1, height = 4, width = 50)
tekst_felt.pack(side=tk.LEFT)
tekst_felt.insert(tk.END,quote)

scrollbar_1 = tk.Scrollbar(frame_1)
scrollbar_1.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar_1.config(command = tekst_felt.yview)
tekst_felt.config(yscrollcommand=scrollbar_1.set)

# Opgave 4
frame_2 = tk.Frame(root)
frame_2.pack()

label_2 = tk.Label(frame_2, text="Indtast navn:")
label_2.pack(side=tk.LEFT, padx=10, pady=10)

entry_felt = tk.Entry(frame_2)
entry_felt.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()