import tkinter as tk

'''
TODO: make a calculator that converts miles to km
'''
window = tk.Tk()
window.minsize(width=500, height=300)
window.title("Mile to Km Converter")
window.config(padx=50, pady=25)

def calculate():
    result_value = round(float(input.get()) * 1.6, 2)
    result["text"] = result_value



# ENTRY FIELD
input = tk.Entry(width=15)
input.grid(column=1, row=0)

# LABELS
miles = tk.Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = tk.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km = tk.Label(text="Km")
km.grid(column=2, row=1)

result = tk.Label(text="0")
result.grid(column=1,row=1)

# BUTTOM
buttom = tk.Button(text="Calculate", command=calculate)
buttom.grid(column=1, row=2)


# Start the main event loop
window.mainloop()
