import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=103, pady=50, bg=YELLOW)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=bg_image)
canvas.pack()
canvas.create_text(103,130, text="00:00", fill="white",font=(FONT_NAME,35,"bold"))



window.mainloop()