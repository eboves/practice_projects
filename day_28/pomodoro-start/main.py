import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps 
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    check_marks.config(text="")
    title.config(text="Timer", fg=GREEN)



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    # if 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Long Break", fg=GREEN, font=(FONT_NAME, 35, "bold"))
    # if 2nd 4th, 6th
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Short Break", fg=PINK, font=(FONT_NAME, 35, "bold"))
    # if 1st 3rd 5th 7th rep:
    else:
        count_down(work_sec)
        title.config(text="WORKING SECTION", fg=RED, font=(FONT_NAME, 35, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10: 
        count_sec == f"0{count_sec}"
    canvas.itemconfig(canvas_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(range/2)
        for _ in range(work_session):
            marks += "✓"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=103, pady=50, bg=YELLOW)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=bg_image)
canvas_text = canvas.create_text(103,130, text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

############## LABELS ##############

# Title
title = tk.Label(text="Timer", fg=GREEN, background=YELLOW, font=(FONT_NAME, 45, "bold"))
title.grid(column=1, row=0)
# Check Marck
check_marks = tk.Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1,row=3)
############## BUTTOMS ##############


#Buttons
start = tk.Button(text="Start", highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)

# Reset
reset = tk.Button(text="Reset", highlightthickness=0,padx=0,pady=0, command=reset_timer)
reset.grid(column=2, row=2)




window.mainloop()