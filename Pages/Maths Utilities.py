import streamlit as st
import base64
import os   
st.set_page_config(page_title="Math Utilities", page_icon="🧮", layout="centered")
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

bg_base64 = get_base64_image("images/background code1.jpg")
if bg_base64:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(10, 25, 47, 0.8), rgba(10, 25, 47, 0.8)), 
                        url("data:image/jpg;base64,{bg_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        div[data-testid="stContainer"] {{
            background-color: rgba(6, 18, 36, 0.6) !important;
            backdrop-filter: blur(8px);
            border: 1px solid rgba(0, 242, 254, 0.3);
            border-radius: 12px;
            padding: 30px;
        }}
        
        .main-title {{
            color: #00F2FE !important;
            font-size: 3rem !important;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
            text-shadow: 0 0 10px rgba(0, 242, 254, 0.5);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
st.markdown(
    """
    <style>
    .main-title {
        color: #FF4B4B;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
page_title = st.title("Math Utilities 🧮")
tab1,tab2,tab3,tab4,tab5,tab6,tab7 = st.tabs(["Factorials", "Calculator", "Prime Numbers","Greatest Between Three Numbers","Fibonacci","Odd_Even","Palindrome and Reverse   Number"])
with tab1:
    st.header("Factorials")
    num = st.slider("Enter a number to calculate its factorial:",1,100,1,key="Fact")
    if st.button("Calculate Factorial"):
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        st.write(f"The factorial of {num} is: {factorial}")
    with st.expander("Factorial Source Code"):
        st.code('''num = st.slider("Enter a number to calculate its factorial:",1,100,1,key="Fact")
if st.button("Calculate Factorial"):
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i
    st.write(f"The factorial of {num} is: {factorial}")''') 
with tab2:
    st.header("Calculator")
    num1 = st.number_input("Enter the first number:", key="cal1")
    num2 = st.number_input("Enter the second number:", key="cal2")
    operation = st.selectbox("Select an operation:", ["Add", "Subtract", "Multiply", "Divide"])
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero is not allowed."
        st.write(f"The result of {operation.lower()} is: {result}")
    with st.expander("Calculator Source Code"):
        st.code('''num1 = st.number_input("Enter the first number:", key="cal1")   
num2 = st.number_input("Enter the second number:", key="cal2")
operation = st.selectbox("Select an operation:", ["Add", "Subtract", "Multiply", "Divide"])
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero is not allowed."
    st.write(f"The result of {operation.lower()} is: {result}")''')
with tab3:
    st.header("Prime Numbers")
    num = st.slider("Enter a number to check if it's prime:", 0,100,1,key="prime")
    if st.button("Check Prime"):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    st.write(f"{num} is not a prime number.")
                    break
            else:
                st.write(f"{num} is a prime number.")
        else:
            st.write(f"{num} is not a prime number.")
    with st.expander("Source Code for Prime Numbers"):
        st.code('''num = st.slider("Enter a number to check if it's prime:", 0,100,1,key="prime")
if st.button("Check Prime"):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                st.write(f"{num} is not a prime number.")
                break
        else:
            st.write(f"{num} is a prime number.")
    else:
        st.write(f"{num} is not a prime number.")''')
with tab4:
    st.header("Greatest Between Three Numbers")
    num1 = st.slider("Enter the first number:", 0,100,1,key="num1")
    num2 = st.slider("Enter the second number:", 0,100,1,key="num2")
    num3 = st.slider("Enter the third number:", 0,100,1,key="num3")
    if st.button("Find Greatest"):
        greatest = max(num1, num2, num3)
        st.write(f"The greatest number among {num1}, {num2}, and {num3} is: {greatest}")
    with st.expander("Source Code for Greatest Between Three Numbers"):
        st.code('''num1 = st.slider("Enter the first number:", 0,100,1,key="num1")
num2 = st.slider("Enter the second number:", 0,100,1,key="num2")
num3 = st.slider("Enter the third number:", 0,100,1,key="   num3")
if st.button("Find Greatest"):  
    greatest = max(num1, num2, num3)
    st.write(f"The greatest number among {num1}, {num2}, and {num3} is: {greatest}")''')
with tab5:
    st.header("Fibonacci")
    num = st.slider("Enter a number to calculate its Fibonacci:", 0,100,1,key="fibo")
    if st.button("Calculate Fibonacci"):
        a, b = 0, 1
        for _ in range(num):
            a, b = b, a + b
        st.write(f"The {num}th Fibonacci number is: {a}")
    with st.expander("Source Code for Fibonacci"):
        st.code('''num = st.slider("Enter a number to calculate its Fibonacci:", 0,100,1,key="fibo")
if st.button("Calculate Fibonacci"):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
    st.write(f"The {num}th Fibonacci number is: {a}")''')

with tab6:
    st.header("Odd or Even")
    num = st.slider("Enter a number to check if it's odd or even:", 0,100,1,key="odd_even")
    if st.button("Check Odd/Even"):
        if num % 2 == 0:
            st.write(f"{num} is an even number.")
        else:
            st.write(f"{num} is an odd number.")
    with st.expander("Source Code for Odd or Even"):
        st.code('''num = st.slider("Enter a number to check if it's odd or even:", 0,100,1,key="odd_even")
if st.button("Check Odd/Even"):
    if num % 2 == 0:
        st.write(f"{num} is an even number.")
    else:
        st.write(f"{num} is an odd number.")''')
with tab7:
    st.header("Palindrome and Reverse Number")
    num = st.slider("Enter a number to check if it's a palindrome and to reverse it:", 0,100,1,key="palindrome")
    if st.button("Check Palindrome and Reverse"):
        str_num = str(num)
        reversed_num = str_num[::-1]
        if str_num == reversed_num:
            st.write(f"{num} is a palindrome number.")
        else:
            st.write(f"{num} is not a palindrome number.")
        st.write(f"The reverse of {num} is: {reversed_num}")    
    with st.expander("Source Code for Palindrome and Reverse Number"):
        st.code('''num = st.slider("Enter a number to check if it's a palindrome and to reverse it:", 0,100,1,key="palindrome") 
if st.button("Check Palindrome and Reverse"):
    str_num = str(num)
    reversed_num = str_num[::-1]
    if str_num == reversed_num:
        st.write(f"{num} is a palindrome number.")
    else:
        st.write(f"{num} is not a palindrome number.")
    st.write(f"The reverse of {num} is: {reversed_num}")''')