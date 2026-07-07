from database import Database
from questions import Question

class Result:

    FILE_NAME = "data/results.json"

    @classmethod
    def submit_test(
        cls,
        student_id,
        test,
        answers
    ):

        questions = Question.get_all_questions() 

        score = 0
        total_marks = 0
        correct = 0
        wrong = 0

        answer_details = []

        for q_id in test["questions"]:
            question = None

            for q in questions:

                if q["question_id"] == q_id:
                    question = q
                    break

            if question is None:
                continue    

            total_marks += question["marks"]

            student_answer = answers.get(str(q_id))

            is_correct = (
                student_answer == question["correct_answer"]
            )

            if is_correct:
                score += question["marks"]
                correct = correct + 1

            else:
                wrong = wrong + 1   


            answer_details.append({
                "question_id":q_id,
                "question":question["question"],
                "student_answer":student_answer,
                "correct_answer":question["correct_answer"],
                "marks":question["marks"],
                "status":"Correct" if is_correct else "Wrong"
            }) 

            perentage = 0

            if total_marks > 0:
                perentage = round(
                    (score / total_marks ) * 100,
                    2
                ) 


            result = {
                "student_id": student_id,
                "test_id" : test["test_id"],
                "test_title":test["title"],
                "score":score,
                "total_marks":total_marks,
                "correct":correct,
                "wrong":wrong,
                "perentage":perentage,
                "answers":answer_details

            }  

            results = Database.load_data(
                cls.FILE_NAME
            ) 

            results.append(result) 

            Database.savedata(
                cls.FILE_NAME,
                results

            )

            return result
        

        @classmethod
        def get_student_result(
            cls,
            student_id
        ):
            
            results = Database.load_data(
                cls.FILE_NAME
            )

            return [

                result

                for result in results
                if result["student_id"] == student_id
            ]





                