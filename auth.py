from database import Database

class Auth:

    FILE_NAME = "data/users.json"

    @staticmethod
    def login(email , password):

        users = Database.load_data(
            Auth.FILE_NAME
        )

        for user in users: 

            if (
                user["email"] == email
                and
                user["password"] == password
            ):

                return user
        return None 


      


          


             