import tkinter

def button_clicked():
    print("Button is clicked")
    my_label["text"] = "Button is clicked"

window = tkinter.Tk()
window.title("1st GUI prgm")
window.minsize(width=500, height=300) # sets minimum window size

# Label
my_label = tkinter.Label(text="this is label 1", font=("Arial", 20, "italic"))
my_label.pack() # this is necessary to display on the screen, packs the label on the screen # center of screen by default

# Other methods:
# my_label["text"] = "New Text"
# my_label.config(text = "Latest Text")

###############
# Buttons:

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

###############
# Entry:

user_input = tkinter.Entry()
# print(user_input.get()) 
user_input.pack()


window.mainloop() # keeps the window open