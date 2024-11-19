class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = self.get_valid_answer(current_question)
        self.check_answer(current_question, user_answer)
        if self.still_has_questions():
            print(f"You've answered {self.score}/{self.question_number} correctly.")
        

    def get_valid_answer(self, current_question):
        valid_inputs = ["True", "False"]
        while True:
            user_input = input(f"Q{self.question_number}. {current_question.text} (True/False)?: ").title()
            if user_input in valid_inputs:
                return user_input
            else:
                print("Invalid input.")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, current_question, user_answer):
        correct_answer = f"The correct answer is: {current_question.answer}"
        if user_answer == current_question.answer:
            self.score += 1
            print(f"Correct! {correct_answer}")
        else:
            print(f"Incorrect! {correct_answer}")
        