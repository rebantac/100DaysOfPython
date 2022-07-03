import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
# print(to_learn)
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) # so that the card is flipped only when the user waits on a card for 4s.

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(4000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


#------------------------------------- UI DESIGN ------------------------------------------#
window = tkinter.Tk()
window.title("FLASH CARD GENERATOR")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(4000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526)
# Card Img
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Cross Button
cross_img = tkinter.PhotoImage(file="images/wrong.png")
unkwown_btn = tkinter.Button(image=cross_img, highlightthickness=0, command=next_card)
unkwown_btn.grid(row=1, column=0)

# Check Button
check_img = tkinter.PhotoImage(file="images/right.png")
kwown_btn = tkinter.Button(image=check_img, highlightthickness=0, command=next_card)
kwown_btn.grid(row=1, column=1)

next_card() # the fnctn is called once so that the french word appears when the window loads up

window.mainloop()