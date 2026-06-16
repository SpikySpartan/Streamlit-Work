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
    page_title="Max Finder",
    page_icon="👑",
    layout="centered"
)

# 2. Custom CSS Styling
st.markdown(
    """
    <style>
    .main-title {
        color: #1E3A8A;
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle {
        color: #6B7280;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 25px;
    }
    div[data-testid="stBlock"] {
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Header Section
st.markdown('<p class="main-title">👑 Find the Greatest Number</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Adjust the sliders below to compare two different values instantly.</p>', unsafe_allow_html=True)

t1=st.slider("First number",1,1000)
t2=st.slider("Second number",1,1000)
if st.button("Find"):
    if t1>t2:
        st.success(f"Greater is First number={t1}")
    else:
         st.success(f"Greater is second number={t2}")
st.subheader("Python Code")
st.code('''import streamlit as st

t1=st.slider("First number",1,1000)
t2=st.slider("Second number",1,1000)
if st.button("Find"):
    if t1>t2:
        st.success(f"Greater is First number={t1}")
    else:
         st.success(f"Greater is second number={t2}")''')