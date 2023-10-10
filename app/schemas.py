from pydantic import BaseModel, EmailStr


class question(BaseModel):
    question : str = "0"
    answer : str ="0"
    level : int ="0"
 
class user(BaseModel):
    email : EmailStr
    password : str
    start_level : int =0
    
    

# class user_data(BaseModel):
#     user_id : int
#     level: int =None

class review(BaseModel):
    user_id : int
    question_id : int
    result : bool =False

class question_view(BaseModel):
    question : str