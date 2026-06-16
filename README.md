# 🧮 Streamlit-Work: Interactive Math Utilities Dashboard

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#license)

A modern, interactive **mathematical utilities dashboard** built with [Streamlit](https://streamlit.io/). This project showcases a collection of elegant Python tools for mathematical computations with a futuristic glassmorphic UI design.

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.9** or higher
- **pip** (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SpikySpartan/Streamlit-Work.git
   cd Streamlit-Work
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add required image assets**
   - Place `background.jpg` in the `images/` folder
   - Place `logo.png` in the `images/` folder
   - These files are essential for the login page styling

### Run the Application

```bash
streamlit run Main.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
Streamlit-Work/
├── Main.py                          # 🔐 Login/Portal page (entry point)
├── Pages/
│   └── Maths Utilities.py          # 📊 Multi-tool dashboard with tabs
├── Basic Codes/                     # 📚 Individual utility modules
│   ├── Factorial.py
│   ├── Generate the table of a number.py
│   ├── Greatest Between Three Number.py
│   ├── Greatest Between Two Numbers.py
│   ├── Odd_Even.py
│   ├── Prime.py
│   ├── Reverse a number and check it is palindrome or not.py
│   └── Sign up.py
├── images/                          # 🖼️ UI Assets
│   ├── background.jpg
│   └── logo.png
├── requirements.txt                 # 📦 Dependencies
├── .gitignore                       # 🚫 Git ignore rules
└── README.md                        # 📖 This file
```

---

## ✨ Features

### 🔐 Main Portal (`Main.py`)
A futuristic login interface featuring:
- Custom glassmorphic CSS styling with cyan accents
- Base64-encoded background and logo images
- Form validation for username/password fields
- Responsive design with centered layout

### 📊 Math Utilities Dashboard (`Pages/Maths Utilities.py`)
An elegant multi-tab interface providing seven specialized mathematical tools:

| # | Tool | Description | Algorithm |
|---|------|-------------|-----------|
| 🔢 | **Factorial Calculator** | Computes factorial sequences (0-100) | Mathematical product n! |
| 🧮 | **Standalone Calculator** | Basic arithmetic operations | Addition, subtraction, multiplication, division |
| 🧬 | **Primality Tester** | Determines if a number is prime | Optimized O(√n) algorithm |
| 👑 | **Vector Maximum Finder** | Finds largest among three numbers | Efficient comparison |
| 📈 | **Fibonacci Calculator** | Generates Fibonacci sequences | Dynamic iterative generation |
| ⚖️ | **Parity Identifier** | Checks if number is odd/even | Modulo operation (n % 2) |
| 🔄 | **Palindrome Validator** | Tests numeric/string palindromes | String reversal & comparison |

---

## 🎨 Design Highlights

### Glassmorphic Theme
The dashboard features a modern **cyberpunk aesthetic** with:
- **Dark translucent panels** with blur effects
- **Cyan neon accents** for visual appeal
- **Base64-encoded assets** (no external dependencies)
- **Responsive widgets** that adapt to all screen sizes

### Custom CSS Styling
```css
background-color: rgba(6, 18, 36, 0.6) !important;
backdrop-filter: blur(8px);
border: 1px solid rgba(0, 242, 254, 0.3);
box-shadow: 0 0 25px rgba(0, 242, 254, 0.15);
```

---

## 💡 Technical Highlights

- **Optimized Algorithms**
  - O(√n) primality testing for efficiency
  - Fast factorial computation with sliders
  - Efficient Fibonacci generation

- **Error Handling**
  - Zero-division protection in calculator
  - Input validation on all forms
  - Graceful image asset fallbacks

- **Modern Architecture**
  - Streamlit multi-page apps structure
  - Modular utility functions
  - Responsive UI components

---

## 🔧 Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Streamlit** | Web application framework |
| **Python 3.9+** | Core programming language |
| **CSS3** | Custom theming and glassmorphism styling |
| **Base64** | Embedded image encoding |

---

## 📋 Requirements

The project requires only one external dependency:

- **streamlit ≥ 1.30.0**

All utilities are built using Python's standard library, ensuring lightweight and fast execution.

---

## 🎯 Usage Examples

### Running Individual Utilities
You can run individual utility files independently:
```bash
# Run factorial calculator
streamlit run "Basic Codes/Factorial.py"

# Run primality tester
streamlit run "Basic Codes/Prime.py"

# Run math utilities dashboard
streamlit run Pages/"Maths Utilities.py"
```

### Accessing via Main Portal
1. Start the app: `streamlit run Main.py`
2. Log in with any username/password
3. Navigate to "Maths Utilities" from the sidebar
4. Select desired tool from tabs

---

## 🐛 Troubleshooting

### Issue: "Image not found" warning on startup
**Solution:** Ensure `background.jpg` and `logo.png` exist in the `images/` folder. The app will still run, but styling will be reduced.

### Issue: Port 8501 already in use
**Solution:** Run on a different port:
```bash
streamlit run Main.py --server.port 8502
```

### Issue: Module not found error
**Solution:** Verify you're in the correct directory and dependencies are installed:
```bash
pip install -r requirements.txt
```

---

## 📚 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Official Docs](https://docs.python.org/3/)
- [CSS Glassmorphism Design](https://css.glass/)

---

## 💬 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature`
3. **Commit** your changes: `git commit -m 'Add your feature'`
4. **Push** to the branch: `git push origin feature/your-feature`
5. **Submit** a pull request

### Contribution Ideas
- Add more mathematical utilities (statistics, calculus, etc.)
- Enhance UI/UX with additional themes
- Add unit tests for utility functions
- Improve documentation and examples

---

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 👨‍💻 Author

**SpikySpartan** - [GitHub Profile](https://github.com/SpikySpartan)

---

## 🌟 Support

If you find this project useful:
- ⭐ **Star** this repository
- 📢 **Share** with others
- 💬 **Open issues** for bugs or feature requests
- 🤝 **Contribute** improvements

---

**Made with ❤️ using Streamlit**
