from fastapi import FastAPI, status, Depends
from datetime import date
from csv import DictReader
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models
import scrap

app = FastAPI()
models.Base.metadata.create_all(engine)
url = "https://www.theverge.com/"


@app.get("/")
def index():
    return {"msg": "server running successfully"}


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close_all()


@app.post("/addToDb", status_code=status.HTTP_200_OK)
async def addToDb(db: Session = Depends(get_db)):
    news_list = scrap.scrap_news_data(url)
    for n in news_list:
        row = models.News(Headline=n.get("Headline", None), Link=n.get("Link", None),
                          Author=n.get("Author", None), Date=n.get("Date", None))
        db.add(row)
        db.commit()
        db.refresh(row)
    return ("Success")
