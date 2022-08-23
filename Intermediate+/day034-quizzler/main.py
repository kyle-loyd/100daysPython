from question_model import Question
from rest_client import get_quiz_questions
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in get_quiz_questions():
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
