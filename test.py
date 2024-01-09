import streamlit as st

def addition_calculator():
    st.title("ADDITION Calculator")

    x = st.number_input("Enter first number:")
    y = st.number_input("Enter second number:")

    add_button = st.button("Add Numbers")

    if add_button:
        sum_result = x + y
        st.success(f"Sum of your numbers is: {sum_result}")

if __name__ == "__main__":
    addition_calculator()



