import starlit
import requests
from starlit import html

class CalculatorApp(starlit.App):
    def __init__(self):
        super().__init__()
        self.result = "0"
        self.number1 = ""
        self.number2 = ""
        self.operator = ""
    
    # Handle button click for numbers and operators
    def handle_button_click(self, value):
        if value in "0123456789":
            if self.operator:
                self.number2 += value
            else:
                self.number1 += value
        elif value in "+-*/":
            self.operator = value
        elif value == "=":
            self.calculate_result()
        elif value == "sqrt":
            self.calculate_result(unary=True)
        elif value == "C":
            self.clear()
    
    # Clear the current inputs and result
    def clear(self):
        self.result = "0"
        self.number1 = ""
        self.number2 = ""
        self.operator = ""

    # Perform the calculation, either unary or binary
    def calculate_result(self, unary=False):
        if unary:  # Unary operation (sqrt)
            response = requests.post(
                "http://localhost:8000/calculate/", json={
                    "number1": float(self.number1),
                    "operator": "sqrt"
                }
            )
        else:  # Binary operation (e.g., addition, subtraction)
            response = requests.post(
                "http://localhost:8000/calculate/", json={
                    "number1": float(self.number1),
                    "number2": float(self.number2),
                    "operator": self.operator
                }
            )
        
        if response.ok:
            self.result = str(response.json().get("result", "Error"))
        else:
            self.result = "Error"
        
        self.number1 = self.result
        self.number2 = ""
        self.operator = ""
    
    # Render the frontend UI
    def render(self):
        return html.div(
            html.h1("Calculator"),
            html.input(id="display", value=self.result, readonly=True),
            html.div(
                *[html.button(value, onclick=f"handle_button_click('{value}')") for value in [
                    '7', '8', '9', '/',
                    '4', '5', '6', '*',
                    '1', '2', '3', '-',
                    '0', '.', '=', '+',
                    'sqrt', 'C'
                ]]
            )
        )

# Run the Starlit app
if __name__ == "__main__":
    CalculatorApp().run()

