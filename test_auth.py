from student import Student 
from auth import Auth

success , message = Student.register (
    2,
    "mayuri",
    "bisen@gmail.com",
    "4567" 
)

print(message)

user = Auth.login(
    "bisen@gmail.com",
    "4567"
)

print (user)

