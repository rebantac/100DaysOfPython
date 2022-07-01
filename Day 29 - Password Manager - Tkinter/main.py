import tkinter
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    username = email_input.get()
    password = password_input.get()

    if(len(website) and len(username) and len(password)):
        is_ok = messagebox.askokcancel(
            title=website, message=f"Details entered: \nEmail: {username} \nPassword: {password} \nClick Ok to confirm")

        if is_ok:
            with open("data.txt", mode="a") as file1:
                file1.write(f"{website} | {username} | {password}\n")
                website_input.delete(0, "end")
                password_input.delete(0, "end")
    else:
        messagebox.showinfo(
            title="Oops", message="Don't leave any fields empty!")

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)

# Lock Img
canvas = tkinter.Canvas(width=200, height=200)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Website Tag:
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = tkinter.Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()  # focuses the cursor on the entry

# Email Tag:
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = tkinter.Entry(width=40)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "rebantachakraborty8@gmail.com")

# Email Tag:
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = tkinter.Entry(width=22)
password_input.grid(column=1, row=3)

generate_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

# Add button
add_button = tkinter.Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
