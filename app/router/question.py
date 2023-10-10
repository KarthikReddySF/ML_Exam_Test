from fastapi import APIRouter,Depends,Request
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas,models
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

router=APIRouter(prefix="/que",tags=["question"])
# operating_directory = os.path.dirname(os.path.abspath(__file__))
# router.mount("/static", StaticFiles(directory="static"), name="static")
# templates=Jinja2Templates(directory="templates/")
# templates = Jinja2Templates(directory=os.path.join(operating_directory, 'templates'))
@router.get("")
def get_data(db : Session=Depends(get_db)):
    data=db.query(models.Question).all()
    return data
@router.post("/posts")
def send_data(post : schemas.question,db : Session=Depends(get_db)):
    new_post=models.Question(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/test/{id}",response_model=list[schemas.question_view])
def display(id: int,db:Session=Depends(get_db)):
    data=db.query(models.User.start_level).filter(models.User.id==id).first()
    # level=data.start_level
    print(data[0])
    new_data=db.query(models.Question).filter(models.Question.level==data[0]).all()
    # p=new_data.question
    return new_data






