from database import Database

class Question:

    FILE_NAME = "data/questions.json"

    def __init__(
            self,
            question_id,
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer,
            marks=1
    ):
        
        self.question_id = question_id
        self.question = question
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.correct_answer = correct_answer
        self.marks = marks

    def to_dict(self):
        return {
            "question_id":self.question_id,
            "question":self.question,
            "option_a":self.option_a,
            "option_b":self.option_b,
            "option_c":self.option_c,
            "option_d":self.option_d,
            "correct_answer":self.correct_answer,
            "marks":self.marks
        }
    @classmethod
    def add_question(
        cls,
        question_id,
        question,
        option_a,
        option_b,
        option_c,
        option_d,
        correct_answer,
        marks

    ):

        questions = Database.load_data(cls.FILE_NAME)

        for q in questions:
            if q ["question_id"] == question_id:
                return False , "Question ID already exists"

        new_question = Question(
            question_id,
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer,
            marks

        )

        questions.append(new_question.to_dict())
        Database.savedata(cls.FILE_NAME,questions)

        return True , "Question Added Successfully"

    @classmethod
    def get_all_questions(cls):
        return Database.load_data(cls.FILE_NAME)

    @classmethod 
    def delete_question(cls,question_id):

        questions = Database.load_data(cls.FILE_NAME)

        updated = []

        found = False

        for question in questions:
            if question["question_id"] != question_id:
                updated.append(question)
            else:
                found = True

        Database.savedata(cls.FILE_NAME,updated)


        return found
                                    
        