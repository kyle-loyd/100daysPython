from tkinter import *


def update_km():
    num_km = "{:.2f}".format(int(mile_entry.get()) * 1.609344)
    num_km_value_label.config(text=num_km)


window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=30, pady=20)

num_miles_label = Label(text="# of miles:")
num_miles_label.grid(row=0, column=0)

num_km_label = Label(text="# of Kilometers:")
num_km_label.grid(row=1, column=0)

mile_entry = Entry()
mile_entry.grid(row=0, column=1)

num_km_value_label = Label()
num_km_value_label.grid(row=1, column=1)

submit_btn = Button(text="Submit", command=update_km)
submit_btn.grid(row=2, column=1)

window.mainloop()
