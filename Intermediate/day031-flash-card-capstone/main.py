from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
WINDOW_PADDING = 50
CARD_FRONT_IMG_PATH = 'images/card_front.png'
CARD_BACK_IMG_PATH = 'images/card_back.png'
UNKNOWN_BTN_IMG_PATH = 'images/wrong.png'
KNOWN_BTN_IMG_PATH = 'images/right.png'
FRENCH_DATA_PATH = 'data/french_words.csv'

to_learn = []
front_is_showing = True


def get_words_to_learn():
    global to_learn
    data = None
    try:
        data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        data = pandas.read_csv("data/french_words.csv")
        data.to_csv("data/words_to_learn.csv", index=False)
    finally:
        to_learn = data.to_dict(orient="records")


def mark_as_known():
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    show_card(card_front_img, "French", "black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    if front_is_showing:
        show_card(card_back_img, "English", "white")
        return
    show_card(card_front_img, "French", "black")


def show_card(img, key, font_color):
    canvas.itemconfig(card, image=img)
    canvas.itemconfig(category_text, text=key, fill=font_color)
    canvas.itemconfig(keyword_text, text=current_card[key], fill=font_color)


window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=WINDOW_PADDING, pady=WINDOW_PADDING)
flip_timer = window.after(3000, func=flip_card)

card_front_img = PhotoImage(file=CARD_FRONT_IMG_PATH)
card_back_img = PhotoImage(file=CARD_BACK_IMG_PATH)
unknown_btn_img = PhotoImage(file=UNKNOWN_BTN_IMG_PATH)
known_btn_img = PhotoImage(file=KNOWN_BTN_IMG_PATH)

canvas = Canvas(window, bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=5)
category_text = canvas.create_text(400, 150, fill="black", font=("Arial", 40, "italic"))
keyword_text = canvas.create_text(400, 263, fill="black", font=("Arial", 60, "bold"))

unknown_button = Button(image=unknown_btn_img, highlightthickness=0, borderwidth=0, command=next_card)
unknown_button.grid(row=1, column=1)
known_button = Button(image=known_btn_img, highlightthickness=0, borderwidth=0, command=mark_as_known)
known_button.grid(row=1, column=3)

get_words_to_learn()
current_card = choice(to_learn)
show_card(card_front_img, "French", "black")

window.mainloop()
