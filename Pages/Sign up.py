import streamlit as st
import base64
import os
import mysql.connector
conn = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="streamlit_test")
mycursor = conn.cursor()
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

bg_base64 = get_base64_image("images/Signup.jpg")

# 2. Inject CSS for Background and Styling
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
st.title("Sign up")
username=st.text_input("Username")
password=st.text_input("Password",type="password")
mobile=st.text_input("Mobile number")
email=st.text_input("Email id")
dob=st.text_input("Date of Birth")
if st.button("Sign up"):
    mycursor.execute("INSERT INTO user_info (username, password, mobile, email, dob) VALUES (%s, %s, %s, %s, %s)", (username, password, mobile, email, dob))
    conn.commit()
    st.write("Welcome", username)
    st.success("Sign up successful")
with st.expander("Sign up Source Code"):
    st.code('''import streamlit as st
st.title("Sign up")
username=st.text_input("Username")
password=st.text_input("Password",type="password")
mobile=st.text_input("Mobile number")
email=st.text_input("Email id")
dob=st.text_input("Date of Birth")
if st.button("Sign up"):
    st.write("Welcome", username)
    st.success("Sign up successful")''')