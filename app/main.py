from fastapi import FastAPI
from . import models
from .database import engine
from .router import question,user,review


app=FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(question.router)

app.include_router(user.router)

app.include_router(review.router)