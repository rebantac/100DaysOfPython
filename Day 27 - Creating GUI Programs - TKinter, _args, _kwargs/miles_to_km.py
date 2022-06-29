import tkinter


def button_clicked():
    new_km = float(miles_input.get()) * 1.6
    km_converted["text"] = new_km


window = tkinter.Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

convert_label = tkinter.Label(text="is equal to")
convert_label.grid(column=0, row=1)

km_converted = tkinter.Label(text=0)
km_converted.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = tkinter.Button(text="Calculate", command=button_clicked)
calc_button.grid(column=1, row=2)

window.mainloop()