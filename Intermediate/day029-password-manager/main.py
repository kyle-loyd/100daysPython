from tkinter import *
from tkinter import messagebox
import password


def populate_generated_password():
    password_entry.delete(0, END)
    password_entry.insert(0, password.generate())


def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password_value = password_entry.get()
    confirmation_msg = f"These are the details entered: \n\nEmail: {username} \nPassword: {password_value} \n\nIs it ok to save?"
    empty_fields_error = "All fields are required"

    if website == "" or username == "" or password_value == "":
        messagebox.showerror(title="Error", message=empty_fields_error)
        return

    data_entry = f"{website} | {username} | {password_value}"

    is_ok = messagebox.askokcancel(title=f"Save Password: {website}", message=confirmation_msg)

    if is_ok:
        with open("data.txt", "a") as data:
            data.write(data_entry)
        website_entry.delete(0, END)
        password_entry.delete(0, END)

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
website_entry.grid(row=1, column=1, columnspan=2, sticky=EW)
website_entry.focus()

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
