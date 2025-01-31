from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

# Define the request body format for the calculator
class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operator: str

# Perform calculation based on operator
@app.post("/calculate")
async def calculate(data: CalculationRequest):
    num1 = data.num1
    num2 = data.num2
    operator = data.operator
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return {"error": "Division by zero is not allowed."}
    else:
        return {"error": f"Invalid operator: {operator}"}
    
    return {"result": result}
