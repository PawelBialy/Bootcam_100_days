from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
   questions_text = questions["text"]
   questions_answer = questions["answer"]
   new_question =Question(questions_text,questions_answer)
   question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
