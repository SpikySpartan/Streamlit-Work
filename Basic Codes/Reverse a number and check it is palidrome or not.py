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
    .main-title {
        color: #1E3A8A;
        font-size: 2.3rem;
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
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Header Setup
st.markdown('<p class="main-title">🔄 Palindrome & Reverse Checker</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Flip digits upside down and verify mathematical symmetry instantly.</p>', unsafe_allow_html=True)
t1=st.slider("Select a number",1,1000)
if st.button("REVERSE"):
    n=t1
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=int(n/10)
    st.success(f"Reverse={s}")
    if s == t1:
        st.success("🎉 **PALINDROME NUMBER** — It reads perfectly identical backward and forward!")
    else:
        st.error("❌ **NOT A PALINDROME NUMBER** — The sequence does not have reflectional symmetry.")
st.subheader("Python Code")
st.code('''import streamlit as st
st.title("Reverse a number and check it is palidrome or not")
t1=st.slider("Select a number",1,1000)
if st.button("REVERSE"):
    n=t1
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=int(n/10)
    st.success(f"Reverse={s}")
    if s==t1:
            st.success("PALINDROME NUMBER")
    else:
            st.success("NOT A PALINDROME NUMBER")''')
