from tkinter import *
import random
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
seen_words = {
    "english": [],
    "france": []
}

################# Load Data #################

france = "French"
english = "English"
rand_choice = {}
df_dict = {}
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    df_dict = original_data.to_dict(orient="records")
else:
    df_dict = df.to_dict("records")

def next_card():
    global rand_choice, flip_timer
    window.after_cancel(flip_timer)
    rand_choice = random.choice(df_dict) 
    card.itemconfig(title, text = france, fill="black")
    card.itemconfig(word, text=rand_choice["French"], fill="black")
    card.itemconfig(image_card, image=card_front)
    flip_timer = window.after(3000, flip_card)
def know_this_one():
    df_dict.remove(rand_choice)
    data = pd.DataFrame(df_dict)
    data.to_csv("data/words_to_learn", index=False)
    next_card()

def flip_card():
    card.itemconfig(image_card, image=card_back)
    card.itemconfig(title, text=english, fill="white")
    card.itemconfig(word, text=rand_choice["English"], fill="white")

################# LOGIC #################


################# UI #################
window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, flip_card)
# --------- canvas ----------
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
image_card = card.create_image(400, 263, image=card_front)
title = card.create_text(400, 150, text="Title", fill='black', font=('Arial', 40, "italic"))
word = card.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)


# --------- buttons ----------
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0,command=next_card) 
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0,command=know_this_one)
right_button.grid(column=1, row=1)


next_card()
window.mainloop()









