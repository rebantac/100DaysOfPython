# WARNING: don't mix .pack() with .grid()
import tkinter


def button_clicked():
    print("Button is clicked")
    new_text = user_input.get() 
    my_label["text"] = new_text


window = tkinter.Tk()
window.title("1st GUI prgm")
window.minsize(width=500, height=300) # sets minimum window size
window.config(padx=50, pady=30) # adds padding all over

my_label = tkinter.Label(text="this is label 1", font=("Arial", 20, "italic"))
# my_label.pack()
# my_label.place(x=100, y=100) # place using coordinates
my_label.grid(column=0, row=0) # relative placement #this the starting point

button = tkinter.Button(text="Click", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=20, pady=20)

button2 = tkinter.Button(text="New Button")
button2.grid(column=2, row=0)

user_input = tkinter.Entry()
user_input.grid(column=3, row=2)


window.mainloop() # keeps the window open