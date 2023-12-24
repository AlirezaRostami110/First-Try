from fastapi import  Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from config import app


students = [{
    'name' : 'Alireza'
    , 'id': 55454
},
{
  'name' : 'Ahmad'
    , 'id': 432154  
}
]


templates = Jinja2Templates('templates')

@app.get('/', response_class= HTMLResponse)
def home(request : Request):
  
  return templates.TemplateResponse('home.html', {'request': request, 'students' : students})