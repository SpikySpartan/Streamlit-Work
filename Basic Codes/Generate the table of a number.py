import streamlit as st
import base64
import os

# 1. Helper function to safely convert local image to Base64
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

bg_base64 = get_base64_image("images/background code1.jpg")

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
st.markdown(
    """
    <style>
    .table-title {
        color: #009688;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<p class="table-title">🧮 Math Table Generator</p>', unsafe_allow_html=True)
st.title("Generate the table of a number")
t1=st.slider("Select a number",1,100)
if st.button("TABLE"):
       for i in range(1,11,1):
              st.write(i*t1)
st.subheader("Python Code")
st.code('''import streamlit as st
st.title("Generate the table of a number")      
t1=st.slider("Select a number",1,100)
if st.button("TABLE"):      
       for i in range(1,11,1):
              st.write(i*t1)''')