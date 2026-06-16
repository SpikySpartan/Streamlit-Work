# Streamlit-Work
# 🧮Math Utilities Multi-Functional Terminal

An advanced, high-performance mathematical dashboard built entirely using the **Streamlit** framework. Enclosed within a single, cohesive interface, this hub utilizes a futuristic, dark glassmorphic theme to deliver an array of computational utility engines—complete with integrated, interactive runtime tabs and live source code inspection panels.
---

## 🌌 Features

This dashboard leverages Streamlit's native tab architecture to segment your processing tools into seven highly specific micro-engines:

* **🔢 Factorials Module:** Computes the mathematical product sequence of descending integers up to $100!$ using responsive sliders.
* **🧮 Standalone Calculator:** Runs continuous floating-point operations covering addition, subtraction, multiplication, and division arrays with built-in zero-division error protections.
* **🧬 Primality Tester:** Implements an optimized square-root ceiling approach ($O(\sqrt{n})$) to quickly determine if a value is composite or prime.
* **👑 Vector Maximum Finder:** Compares a sequence of three custom inputs simultaneously to cleanly isolate the absolute largest integer.
* **📈 Fibonacci Calculator:** Computes dynamic element sequence paths using tuple variable updates (`a, b = b, a + b`).
* **⚖️ Parity Identifier:** Fast-checks integer modulos to determine if an input is explicitly odd or even.
* **🔄 Symmetry & Reversal Validator:** Translates integers into sequence matrices to calculate reversals and verify string palindromes via index slicing slices (`[::-1]`).

---

## 🖼️ Architectural & Theme Layout

The front-end design uses explicit style overrides to completely strip away standard, plain web defaults and apply a premium tech look:

* **Embedded Memory Assets (Base64):** The app reads your local image pathway (`images/background code1.jpg`) and parses it directly into a memory data vector, preventing missing asset errors regardless of the hosting machine's operating system.
* **Cyber Glass Panels:** Custom CSS selectors target background sheets and user widgets to create a beautiful unified dark interface:
  ```css
  background-color: rgba(6, 18, 36, 0.6) !important;
  backdrop-filter: blur(8px);
  border: 1px solid rgba(0, 242, 254, 0.3);
Python codes
# 📂 Standalone Python Code Utilities Repository

Welcome to the **Basic Codes** core directory. This segment of the project houses an organized suite of independent, responsive mathematical utilities and configuration scripts built using the **Streamlit** framework. Every tool operates as an isolated file containing dedicated, local computer vision/base64 background injection wrappers, stylized alert containers, and real-time code preview pipelines.

![Python Version](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Streamlit UI Engine](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit)

---

## 🛠️ Module Pipeline Directory

Below is the complete architectural mapping of the underlying script inventory, including operational scope and execution notes:

### 1. 🔢 Factorial Calculator (`Factorial.py`)
* **Core Action:** Computes the mathematical product of all positive integers descending down to 1 ($n!$).
* **Features:** Utilizes responsive `st.slider` configurations ranging up to 100 alongside internal layout string formatting hooks.

### 2. 🧮 Matrix Generation Engine (`Generate the table of a number.py`)
* **Core Action:** Spawns a multi-iteration multiplication chart mapping elements cleanly across standard increments ($1 \times n$ through $10 \times n$).
* **Features:** Leverages explicit loop counters formatted inside sequential text block layouts.

### 3. 👑 Triple Coordinate Vector Maximum (`Greatest Between Three Number.py`)
* **Core Action:** Processes three distinct input data points to isolate the absolute dominant integer value.
* **Features:** Employs Python’s native, high-efficiency evaluation operator matrix (`max(t1, t2, t3)`).

### 4. ⚖️ Dual Coordinate Maximum (`Greatest Between Two Numbers.py`)
* **Core Action:** Compares a pair of user-configured slider entries to cleanly branch layout alerts based on a basic arithmetic condition hierarchy.

### 5. 🔢 Integer Parity Identifier (`Odd_Even.py`)
* **Core Action:** Evaluates integer configurations to determine mathematical parity (Modulo evaluation tracking: $n \pmod 2 == 0$).
* **Features:** Instantly flags parity metrics using clean, color-coded visual feedback modules.

### 6. 🧬 Primality Verification Scanner (`Prime.py`)
* **Core Action:** Checks if a chosen integer qualifies as a prime number by iterating through potential factors up to the given boundary ceiling.
* **Features:** Uses an element tracking layout to display a positive flag indicator only when exactly two factors are verified.

### 7. 🔄 Numeric Symmetry Engine (`Reverse a number and check it is palidrome or not.py`)
* **Core Action:** Breaks down an integer to reverse its digital order, then runs reflectional symmetry cross-checks.
* **Features:** Features structural `while` parsing loops combined with alternate high-efficiency string sequence formatting steps (`[::-1]`).

### 📝 Client Sign-Up Gate (`Sign up.py`)
* **Core Action:** A clean mockup dashboard for user profile data input tracking.
* **Features:** Captures user properties with masked input fields (`type="password"`), inline placeholder data, and pop-up registration success metrics.

---
Directory Architecture  
📁 multipages/                             # Your main root project folder on your Desktop
│
├── 📄 Main.py                            # Your central landing page or portal login screen
│
├── 📁 images/                            # Storage for your background graphics
│   ├── 🖼️ background code.jpg
│   ├── 🖼️ background code1.jpg
│   └── 🖼️ background code2.jpg
│
├── 📁 pages/                             # Handles your automatic multi-page sidebar navigation
│   ├── 📄 1_🧮_math_utilities.py         # Your styled tabbed math utilities app
│
└── 📁 basic_codes/                        # NEW: Folder for your standalone Python scripts
    ├── 📄 Factorial.py
    ├── 📄 Generate the table of a number.py
    ├── 📄 Greatest Between Three Number.py
    ├── 📄 Greatest Between Two Numbers.py
    ├── 📄 Odd_Even.py
    ├── 📄 Prime.py
    └── 📄 Reverse a number and check it is palidrome or not.py
