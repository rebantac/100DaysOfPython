import tkinter

BACKGROUND_COLOR = "#B1DDC6"

window = tkinter.Tk()
window.title("FLASH CARD GENERATOR")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = tkinter.Canvas(width=800, height=526)
# Card Front
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)

canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Cross Button
cross_img = tkinter.PhotoImage(file="images/wrong.png")
unkwown_btn = tkinter.Button(image=cross_img, highlightthickness=0)
unkwown_btn.grid(row=1, column=0)

# Check Button
check_img = tkinter.PhotoImage(file="images/right.png")
kwown_btn = tkinter.Button(image=check_img, highlightthickness=0)
kwown_btn.grid(row=1, column=1)


window.mainloop()