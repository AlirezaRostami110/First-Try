from pydantic import BaseModel
from datetime import date

class StudentCreat(BaseModel):
    name : str
    subject : str
    un_id : int
    verify_date : date

class StudentUpdate(StudentCreat):
    pass


class Student(StudentCreat):
    id : int
    
    class config:
        orm_mode = True 