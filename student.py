from database import Database

class Student:

    FILE_NAME = "data/users.json"

    def __init__(
        self,
        student_id,
        name,
        email,
        password,
        role="student"
    ):
        self.student_id = self.student_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def to_dict(self):

        return{
            "student_id" : self.student_id,
            "name" : self.name,
            "email" : self.email,
            "password" : self.password,
            "role" : self.role
        }
    @classmethod
    def register(
        cls,
        student_id,
        name,
        email,
        password,
    ):

        users = Database.load_data(
            cls.FILE_NAME

        )

        for user in users:
            if user["email"] == email:
                return False , "Email already exists"
        student = Student (
            student_id,
            name,
            email,
            password
        )

        users.append(
            student.to_dict()
        )
        Database.savedata(
            cls.FILE_NAME,
            user
        )
        return True, "Registration Successfully"                       
