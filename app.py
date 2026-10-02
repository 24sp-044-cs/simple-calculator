import streamlit as st

st.set_page_config(page_title="Simple Calculator", page_icon="🧮")

st.title("🧮 Simple Calculator")
st.write("Enter two numbers, choose an operation, and click Calculate to see the result.")

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("First number", value=0.0, format="%.4f")
with col2:
    num2 = st.number_input("Second number", value=0.0, format="%.4f")

operation = st.selectbox(
    "Operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)", "Power (^)", "Modulus (%)"],
)

if st.button("Calculate"):
    if operation.startswith("Addition"):
        result = num1 + num2
    elif operation.startswith("Subtraction"):
        result = num1 - num2
    elif operation.startswith("Multiplication"):
        result = num1 * num2
    elif operation.startswith("Division"):
        if num2 == 0:
            st.error("Error: Division by zero is not allowed.")
            st.stop()
        result = num1 / num2
    elif operation.startswith("Power"):
        result = num1 ** num2
    else:
        if num2 == 0:
            st.error("Error: Modulus by zero is not allowed.")
            st.stop()
        result = num1 % num2

    st.success(f"Result: {result}")
