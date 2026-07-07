from database import Database

class Test:

    FILE_NAME = "data/tests.json"

    def __init__(
        self,
        test_id,
        title,
        duration,
        questions

    ):
        
        self.test_id = test_id
        self.title = title
        self.duration = duration
        self.questions = questions

    def to_dict(self):

        return {

            "test_id": self.test_id,
            "title": self.title,
            "duration":self.duration,
            "questions":self.questions

        }  

    @classmethod

    def create_test(
        cls,
        test_id,
        title,
        duration,
        questions

    ):
        
        tests = Database.load_data(cls.FILE_NAME)

        for test in tests:
            if test["test_id"] == test_id:
                return False , "Test is already exists"
            
        new_test = Test(
             test_id,
             title,
             duration,
             questions
        )   

        tests.append(
            new_test.to_dict()
        ) 

        Database.savedata(
            cls.FILE_NAME,
            tests
        )

        return True, "Test Created Successfully"
    
    @classmethod
    def get_all_tests(cls):

         return Database.load_data(
            cls.FILE_NAME
        )  

    @classmethod
    def get_test(cls,test_id):

        tests =  Database.load_data(
            cls.FILE_NAME
        )
    
        for test in tests:
            
            if test["test_id"] == test_id:
                return test
            
        return None 
    

    @classmethod


    def delete_test(cls,test_id):

        tests = Database.load_data(
            cls.FILE_NAME
        )

        updated = []
        found = False

        for test in tests:
            if test["test_id"] != test_id:
                updated.append(test)
            else:
                found = True  

        Database.savedata(
            cls.FILE_NAME,
            updated
        )  

        return found        



            