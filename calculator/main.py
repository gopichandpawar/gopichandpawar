from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
import math

app = FastAPI()

# Set up the Jinja2 template directory
templates = Jinja2Templates(directory="templates")

# Define the calculation endpoint
@app.get("/calculate")
async def calculate(expression: str):
    try:
        # Safe evaluation of the expression
        result = eval(expression, {"__builtins__": None}, {"sqrt": math.sqrt, "pow": math.pow})
        return {"result": result}
    except Exception as e:
        return {"result": f"Error: {str(e)}"}

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
