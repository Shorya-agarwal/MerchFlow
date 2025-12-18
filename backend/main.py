from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware # <--- NEW IMPORT
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
import models
from database import engine, get_db
from ai_service import categorize_expense

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# --- CORS CONFIGURATION (THE FIX) ---
origins = [
    "http://localhost:5173", # Your React App
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods (POST, GET, OPTIONS, etc.)
    allow_headers=["*"],
)
# ------------------------------------

# Pydantic Models
class TransactionCreate(BaseModel):
    description: str
    amount: float
    user_id: int

class TransactionResponse(BaseModel):
    id: int
    description: str
    amount: float
    category: str
    date: Optional[str] = None # simplified for response

    class Config:
        orm_mode = True

@app.get("/")
def read_root():
    return {"message": "SmartFinance Backend is Running"}

@app.post("/transactions/")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    # 1. AI Categorization
    ai_category = categorize_expense(transaction.description)
    
    # 2. Save to DB
    db_transaction = models.Transaction(
        description=transaction.description,
        amount=transaction.amount,
        category=ai_category,
        user_id=transaction.user_id
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@app.get("/transactions/")
def read_transactions(db: Session = Depends(get_db)):
    # Get all transactions, newest first
    return db.query(models.Transaction).order_by(models.Transaction.id.desc()).all()