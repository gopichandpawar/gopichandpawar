from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import math

app = FastAPI()

# Function to evaluate the expression
def calculate(expression: str) -> str:
    try:
        # Safe evaluation of the expression
        result = eval(expression, {"__builtins__": None}, {"math": math})
        return str(result)
    except Exception as e:
        return "Error"

# Serve the HTML page for the calculator
@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f4f4f4;
            }
            .calculator {
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                padding: 20px;
            }
            input[type="text"] {
                width: 100%;
                height: 50px;
                font-size: 2em;
                text-align: right;
                padding: 10px;
                border: 2px solid #ccc;
                border-radius: 5px;
                margin-bottom: 20px;
            }
            button {
                width: 50px;
                height: 50px;
                font-size: 1.5em;
                margin: 5px;
                border: none;
                background-color: #f0f0f0;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #e0e0e0;
            }
        </style>
    </head>
    <body>
        <div class="calculator">
            <input id="result" type="text" disabled placeholder="0" />
            <div class="buttons">
                <button onclick="addToResult('1')">1</button>
                <button onclick="addToResult('2')">2</button>
                <button onclick="addToResult('3')">3</button>
                <button onclick="addToResult('4')">4</button>
                <button onclick="addToResult('5')">5</button>
                <button onclick="addToResult('6')">6</button>
                <button onclick="addToResult('7')">7</button>
                <button onclick="addToResult('8')">8</button>
                <button onclick="addToResult('9')">9</button>
                <button onclick="addToResult('0')">0</button>
                <button onclick="clearResult()">C</button>

                <button onclick="addToResult('+')">+</button>
                <button onclick="addToResult('-')">-</button>
                <button onclick="addToResult('*')">*</button>
                <button onclick="addToResult('/')">/</button>
                <button onclick="addToResult('%')">%</button>
                <button onclick="addToResult('**')">^</button>

                <button onclick="calculateResult()">=</button>
            </div>
        </div>

        <script>
            let expression = '';

            function addToResult(value) {
                expression += value;
                document.getElementById('result').value = expression;
            }

            function clearResult() {
                expression = '';
                document.getElementById('result').value = '';
            }

            async function calculateResult() {
                const response = await fetch('/calculate/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ expression: expression })
                });

                const result = await response.json();
                document.getElementById('result').value = result.result;
                expression = result.result;
            }
        </script>
    </body>
    </html>
    """

# Handle the calculation logic
@app.post("/calculate/")
async def calculate_expression(expression: str):
    result = calculate(expression)
    return {"result": result}

