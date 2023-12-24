from fastapi import  Request, APIRouter, Depends
from fastapi.templating import Jinja2Templates
from dependencies import get_db
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from schemas import schemas as schemas
from models import student as models


students = [{
    'name' : 'Alireza Rostami'
    , 'id': 40231003
},
{
  'name' : 'Jack sheferd'
    , 'id': 40145001  
},
{
  'name' : 'Alireza Ramezani'
    , 'id': 9734004  
},
{
  'name' : 'Sajjad Jabbaroph'
    , 'id': 666  
}]


router = APIRouter()


templates = Jinja2Templates('templates')

@router.get('/', response_class= HTMLResponse)
def home(request : Request):
  
  return templates.TemplateResponse('home.html', {'request': request, 'students' : students})


@router.get('/details/{st_id}', response_class=HTMLResponse)
def details(request : Request, st_id : int, db: Session = Depends(get_db)):
    student = db.query(models.Student).get(st_id)
    return templates.TemplateResponse('details.html', {'request' : request, 'student' : student})


