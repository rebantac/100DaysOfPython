class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    
    def still_has_question(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

        # Refactored below:
        return self.question_number < len(self.question_list)
    
    
    def check_answer(self, given_answer, correct_answer):
        if given_answer.lower() == correct_answer.lower():
            print("Correct answer!")
            self.score += 1
        else:
            print("Wrong answer!")
        print(f"Correct answer: {correct_answer}")
        print(f"Current Score: {self.score}/{self.question_number}")
        print("\n")

    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        given_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(given_answer, current_question.answer)
        