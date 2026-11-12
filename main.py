from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Expense Tracker", description="A simple expense tracking API", version="1.0.0")

class Expense(BaseModel):
    category: str
    amount: float

@app.get("/")
def home():
    return{"messsage": "Welcome to the Expense Tracker API!"}

@app.post("/calculate")
def calculate_total(expenses: list[Expense]):
    total = sum(expense.amount for expense in expenses)
    return {
        "total_expenses": len(expenses),
        "total_amount": round(total, 2),
        "currency": "GHS",
    }
