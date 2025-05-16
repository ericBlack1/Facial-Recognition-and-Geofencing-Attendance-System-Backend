from sqlalchemy import text
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/ping-db")
def ping_db(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        if result and result[0] == 1:
            return {"status": "Database connected successfully"}
        else:
            return {"status": "Database connection failed"}
    except Exception as e:
        return {"error": str(e)}
