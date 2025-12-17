from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from ai_service import categorize_expense # Import our new AI tool
import models
from database import engine, get_db

# This line creates the tables in the database automatically
models.Base.metadata.create_all(bind=engine)

# Schema for incoming data (what the frontend sends)
class TransactionCreate(BaseModel):
    description: str
    amount: float
    user_id: int

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "SmartFinance Database is Connected!"}

# --- Quick Test Endpoint to Create a User ---
@app.post("/users/")
def create_user(email: str, password: str, db: Session = Depends(get_db)):
    # CAUTION: In real apps, we hash passwords first. This is just a connection test.
    user = models.User(email=email, hashed_password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# --- Quick Test Endpoint to Get Users ---
@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@app.post("/transactions/")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    # 1. Call the AI service to get the category automatically
    ai_category = categorize_expense(transaction.description)
    
    # 2. Create the database record
    db_transaction = models.Transaction(
        description=transaction.description,
        amount=transaction.amount,
        category=ai_category, # This comes from AI!
        user_id=transaction.user_id
    )
    
    # 3. Save to DB
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    
    return db_transaction


@app.get("/transactions/")
def read_transactions(db: Session = Depends(get_db)):
    return db.query(models.Transaction).all()