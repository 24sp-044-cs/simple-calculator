import streamlit as st

st.set_page_config(page_title="Simple Calculator", page_icon="🧮")

st.title("🧮 Simple Calculator")
st.write("Do numbers enter karein, operation chunein aur result dekhein.")

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
            st.error("Error: Zero se divide nahi kar sakte!")
            st.stop()
        result = num1 / num2
    elif operation.startswith("Power"):
        result = num1 ** num2
    else:
        if num2 == 0:
            st.error("Error: Zero se modulus nahi ho sakta!")
            st.stop()
        result = num1 % num2

    st.success(f"Result: {result}")