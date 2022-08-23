from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE_FONT = ("Arial", 11, "bold")
QUESTION_FONT = ("Arial", 18, "italic")
TRUE_BTN_IMG_PATH = "images/true.png"
FALSE_BTN_IMG_PATH = "images/false.png"
PLACEHOLDER_TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(
            text=f"Score: {self.quiz.score}",
            fg="white",
            bg=THEME_COLOR,
            font=SCORE_FONT)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, bg="white", width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(
            150, 125,
            fill="black",
            font=QUESTION_FONT,
            text=PLACEHOLDER_TEXT,
            width=250)

        self.true_button_img = PhotoImage(file=TRUE_BTN_IMG_PATH)
        self.true_button = Button(
            image=self.true_button_img,
            command=self.answer_question_true)
        self.true_button.grid(row=2, column=0, padx=10)

        self.false_button_img = PhotoImage(file=FALSE_BTN_IMG_PATH)
        self.false_button = Button(
            image=self.false_button_img,
            command=self.answer_question_false)
        self.false_button.grid(row=2, column=1, padx=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def answer_question_false(self):
        self.answer_question(False)

    def answer_question_true(self):
        self.answer_question(True)

    def answer_question(self, answer):
        self.quiz.check_answer(answer)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()