from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from os import system

question_bank = []
for datapoint in question_data:
    question_bank.append(Question(datapoint["text"], datapoint["answer"]))

system("cls||clear")
quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()
print(f"You've completed the quiz! Final score: {quiz_brain.score}/{len(quiz_brain.question_list)}")