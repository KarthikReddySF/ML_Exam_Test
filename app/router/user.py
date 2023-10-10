from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas,models

router=APIRouter(prefix="/user",tags=["user"])

@router.get("/")
def get_users(db:Session=Depends(get_db)):
    data=db.query(models.User).all()
    return data

@router.post("/post")
def create_user(data:schemas.user,db:Session=Depends(get_db)):
    new_post=models.User(**data.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post