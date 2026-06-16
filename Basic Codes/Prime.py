import streamlit as st
import base64
import os

# 1. Helper function to safely convert local image to Base64
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

bg_base64 = get_base64_image("images/background code.jpg")

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
st.set_page_config(
    page_title="Prime Number Checker",
    page_icon="🔢",
    layout="centered"
)
st.markdown('<p class="main-title">🔢 Prime Number Checker</p>', unsafe_allow_html=True)
n=st.slider("Pick a number",1,100)
if st.button("Check"):
       f=0
       for i in range(1,n+1):
              if n%i==0:
                     f=f+1#2,3

       if f==2:
              st.success("PRIME")
       else:
              st.success("NOT PRIME")
st.subheader("Python Code")
st.code('''import streamlit as st
n=st.slider("Pick a number",1,100)#5,6
if st.button("Check"):
       f=0
       for i in range(1,n+1):
              if n%i==0:
                     f=f+1#2,3

       if f==2:
              st.success("PRIME")
       else:
              st.success("NOT PRIME")''')