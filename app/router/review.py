from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas,models

router=APIRouter(
    prefix="/review",
    tags=["Review"]
)

@router.get("")
def get_review(db:Session=Depends(get_db)):
    data=db.query(models.Review).all()
    return data

@router.post("/post")
def create_review(data:schemas.review,db:Session=Depends(get_db)):
    new_post=models.Review(**data.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post