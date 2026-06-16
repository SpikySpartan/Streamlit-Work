# 🧮 Streamlit-Work: Math Utilities Dashboard

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#)

An elegant, high-performance **mathematical dashboard** built with [Streamlit](https://streamlit.io/). This repository contains a collection of interactive Python utilities for mathematical computations with a modern glassmorphic UI design.

---

## 🌟 Features

The dashboard leverages Streamlit's tab architecture to provide seven specialized mathematical tools:

| Module | Description | Capability |
|--------|-------------|-----------|
| 🔢 **Factorial Calculator** | Computes factorial sequences (up to 100!) | Interactive sliders, fast computation |
| 🧮 **Standalone Calculator** | Floating-point arithmetic operations | Addition, subtraction, multiplication, division with error protection |
| 🧬 **Primality Tester** | Determines prime vs. composite numbers | Optimized O(√n) algorithm |
| 👑 **Vector Maximum Finder** | Finds the largest among three numbers | Instant comparison with visual feedback |
| 📈 **Fibonacci Calculator** | Generates Fibonacci sequences | Dynamic element generation |
| ⚖️ **Parity Identifier** | Checks if numbers are odd/even | Instant modulo verification |
| 🔄 **Palindrome Validator** | Tests for number/string palindromes | Reversal and symmetry detection |

---

## 🎨 Design Highlights

The UI features a modern **dark glassmorphic theme** with:

✨ **Custom CSS Styling:**
- Embedded Base64 background images (no external asset dependencies)
- Cyber glass panels with blur effects
- Dynamic cyan accent borders
- Responsive widget theming

```css
background-color: rgba(6, 18, 36, 0.6) !important;
backdrop-filter: blur(8px);
border: 1px solid rgba(0, 242, 254, 0.3);
```

---

## 📁 Basic Code

### Core Utilities

#### 1️⃣ **Factorial.py**
- Computes n! (factorial)
- Uses responsive slider input (0-100)
- Mathematical product of descending integers

#### 2️⃣ **Generate the table of a number.py**
- Creates multiplication tables
- Generates 1×n through 10×n matrices
- Formatted sequential layout

#### 3️⃣ **Greatest Between Three Number.py**
- Compares three inputs
- Returns maximum value efficiently
- Python's native `max()` operator

#### 4️⃣ **Greatest Between Two Numbers.py**
- Dual-input comparison
- Slider-based configuration
- Conditional branching with alerts

#### 5️⃣ **Odd_Even.py**
- Parity detection (odd/even)
- Modulo operation: n mod 2 == 0
- Color-coded visual feedback

#### 6️⃣ **Prime.py**
- Primality verification
- Factors up to √n boundary
- Boolean prime/composite flag

#### 7️⃣ **Reverse a number and check it is palindrome or not.py**
- Numeric reversal
- String sequence formatting (`[::-1]`)
- Palindrome symmetry validation

#### 🗝️ **Sign up.py**
- User profile entry mockup
- Masked password fields
- Registration feedback system

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.9+
Streamlit >= 1.30
```

### Installation
```bash
git clone https://github.com/SpikySpartan/Streamlit-Work.git
cd Streamlit-Work
pip install -r requirements.txt
```

### Run the Dashboard
```bash
streamlit run app.py
```

---

## 💡 Technical Highlights

- **Optimized Algorithms:** O(√n) primality testing, efficient Fibonacci generation
- **Error Handling:** Zero-division protection in calculator module
- **Responsive Design:** Adaptive UI with Streamlit's native components
- **Modern Aesthetics:** Glassmorphism with CSS overrides
- **No External Assets:** Base64-encoded background images for reliability

---

## 📊 Architecture

```
Streamlit-Work/
├── README.md
├── requirements.txt
├── Factorial.py
├── Generate the table of a number.py
├── Greatest Between Three Number.py
├── Greatest Between Two Numbers.py
├── Odd_Even.py
├── Prime.py
├── Reverse a number and check it is palindrome or not.py
├── Sign up.py
└── images/
    └── background code1.jpg
```

---

## 🔧 Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web app framework
- **Python 3.9+** - Core programming language
- **CSS** - Custom theming and styling

---

## 💬 Contributing

Contributions, issues, and feature requests are welcome! Feel free to:
- Fork the repository
- Create a feature branch
- Submit pull requests

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**SpikySpartan** - [GitHub Profile](https://github.com/SpikySpartan)

---

**⭐ If you find this project useful, please consider giving it a star!**
