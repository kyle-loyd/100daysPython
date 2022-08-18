import json
from tkinter import *
from tkinter import messagebox
import generator


def populate_generated_password():
    password_entry.delete(0, END)
    password_entry.insert(0, generator.generate())


def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password_value = password_entry.get()
    empty_fields_error = "All fields are required"
    new_data = {
        website: {
            "username": username,
            "password": password_value
        }
    }

    if website == "" or username == "" or password_value == "":
        messagebox.showerror(title="Error", message=empty_fields_error)
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


def search_records():
    website = website_entry.get()
    messagebox_title = f"Find Record: {website}"
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            entry = data[website]
            messagebox_message = f"Username: {entry['username']}\nPassword: {entry['password']}"
    except FileNotFoundError:
        messagebox.showerror(title=messagebox_title, message="No records found.")
        return
    except KeyError:
        messagebox.showinfo(title=messagebox_title, message="No record found under that name.")
    else:
        messagebox.showinfo(title=messagebox_title, message=messagebox_message)


# ---------------------------- UI SETUP ------------------------------- #


LABEL_RIGHT_SPACING = (0, 10)
LABEL_VERTICAL_SPACING = 5

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(window, width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky=E, padx=LABEL_RIGHT_SPACING, pady=LABEL_VERTICAL_SPACING)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=1, sticky=EW)
website_entry.focus()
generate_button = Button(text="Search", command=search_records)
generate_button.grid(row=1, column=2, sticky=EW, padx=(10, 0))

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky=E, padx=LABEL_RIGHT_SPACING, pady=LABEL_VERTICAL_SPACING)
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky=EW)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky=E, padx=LABEL_RIGHT_SPACING, pady=LABEL_VERTICAL_SPACING)
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky=EW)
generate_button = Button(text="Generate Password", command=populate_generated_password)
generate_button.grid(row=3, column=2, sticky=EW, padx=(10, 0))

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()
