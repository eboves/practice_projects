

# # lista = [1,2,3,4]
# def add(*args):
#     total = 0
#     for n in args:
#         total = total + n
#     return total
# totalito = add(1,2,3,4)
# print(f"total sum is: {totalito}")

# from tkinter import *
import tkinter as tk
window = tk.Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)

def clicked():
    # my_label["text"] = "I got cliiiickedddd"
    # print("I got clicked")
    my_label["text"] = inp.get()
# Label: this is a regular text that appears in the screen
my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Entry is a input field. to get hold of the value use the .get() method
inp = tk.Entry(width=10)
inp.grid(column=3, row=2)

# this is a buttom. the command calls the function that handle the event when button is clicked
button = tk.Button(text="click me", command=clicked)
button.grid(column=1, row=1)

button = tk.Button(text="adios")
button.grid(column=2, row=0)


# Start the main event loop
window.mainloop()