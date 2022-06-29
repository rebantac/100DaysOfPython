import tkinter


def button_clicked():
    print("Button is clicked")
    new_text = user_input.get() 
    my_label["text"] = new_text


window = tkinter.Tk()
window.title("1st GUI prgm")
window.minsize(width=500, height=300) # sets minimum window size

my_label = tkinter.Label(text="this is label 1", font=("Arial", 20, "italic"))
my_label.pack()

button = tkinter.Button(text="Click", command=button_clicked)
button.pack()

user_input = tkinter.Entry()
user_input.pack()


window.mainloop() # keeps the window open