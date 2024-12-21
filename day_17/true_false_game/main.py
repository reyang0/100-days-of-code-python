from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
	new_text = question['text']
	new_answer = question['answer']
	new_question = Question(new_text,new_answer)
	question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
	quiz.next_question()

quiz.final_score()
