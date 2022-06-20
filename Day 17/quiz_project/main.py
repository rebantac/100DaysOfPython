from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for item in question_data:
    new_qn = Question(item["text"], item["answer"])
    question_bank.append(new_qn)

# print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Final Score: {quiz.score}/{quiz.question_number}")