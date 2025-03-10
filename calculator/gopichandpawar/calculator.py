import starlit as st
import requests

# Function to update the result in the frontend
def update_result(result):
    st.write(f"Result: {result}")

# Create the calculator UI
def create_calculator():
    st.title("Simple Calculator")

    # Create input fields for numbers
    num1 = st.number_input("Enter first number", value=0)
    num2 = st.number_input("Enter second number", value=0)

    # Create buttons for binary operators (+, -, *, /)
    operator = st.selectbox("Select Operator", ["+", "-", "*", "/", "sqrt"])

    # Create a calculate button
    if st.button("Calculate"):
        # Send the calculation request to FastAPI backend
        response = requests.post(
            "http://localhost:8000/calculate", 
            json={"num1": num1, "num2": num2, "operator": operator}
        )
        data = response.json()
        
        # Show result or error
        if 'result' in data:
            update_result(data['result'])
        else:
            st.error(data['error'])

# Call the create_calculator function to generate the UI
create_calculator()
