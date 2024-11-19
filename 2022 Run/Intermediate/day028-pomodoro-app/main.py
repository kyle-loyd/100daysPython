from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#03af72"
YELLOW = "#f7f5dd"
FONT_NAME = "System"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark_text = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    adjust_ui(bg=YELLOW, title="TIMER", reset_ui=True)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    start_button.config(state="disabled")
    global reps
    reps += 1

    if reps > 8:
        reset_timer()
        return

    elif reps % 8 == 0:
        adjust_ui(bg=RED, title="BREAK", add_check=True)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        adjust_ui(bg=RED, title="BREAK", add_check=True)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        adjust_ui(bg=GREEN, title="FOCUS")
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    minutes = math.floor(count / 60)
    seconds = math.floor(count % 60)
    minutes_string = str(minutes) if minutes > 9 else f'0{minutes}'
    seconds_string = str(seconds) if seconds > 9 else f'0{seconds}'
    time_left = f"{minutes_string}:{seconds_string}"
    canvas.itemconfig(timer_text, text=time_left)
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


def adjust_ui(bg, title, reset_ui=False, add_check=False):
    global checkmark_text
    window.config(bg=bg)
    canvas.config(bg=bg)
    timer_label.config(text=title, bg=bg)
    checkmark_label.config(bg=bg)
    if reset_ui:
        start_button.config(state="normal")
        canvas.itemconfig(timer_text, text="25:00")
        checkmark_text = ""
    if add_check:
        checkmark_text = f"{checkmark_text}✔ "
    checkmark_label.config(text=checkmark_text)


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=35, bg=YELLOW)

tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(window, width=200, height=223, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="TIMER")
timer_label.config(font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg="black")
timer_label.grid(row=0, column=1)

start_button = Button(text="START", highlightthickness=0, command=start_timer)
start_button.config(font=(FONT_NAME, 10, "bold"), padx=2, pady=2)
start_button.grid(row=2, column=0)

reset_button = Button(text="RESET", highlightthickness=0, command=reset_timer)
reset_button.config(font=(FONT_NAME, 10, "bold"), padx=2, pady=2)
reset_button.grid(row=2, column=2)

checkmark_label = Label(fg="black", bg=YELLOW)
checkmark_label.config(font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(row=2, column=1)

window.mainloop()
