# 🐍 Learn Python — From Zero to Hero

> A complete, beginner-friendly Python course with hands-on examples and real projects.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Beginner](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 📖 What You'll Learn

| Level | Topics |
|-------|--------|
| **Beginner** | Variables, Data Types, Operators, Input/Output |
| **Intermediate** | Control Flow, Functions, Data Structures, File Handling |
| **Advanced** | OOP, Error Handling, Modules, Lambda Functions |
| **Expert** | Web APIs (FastAPI, Flask), LLM Architecture, Fine-tuning |

---

## 📁 Project Structure

```
python-learning/
├── basics/                 # Start here! Python fundamentals
│   ├── 01_introduction/    # Your first Python programs
│   ├── 02_variables_types/ # Variables, operators, type conversion
│   ├── 03_control_flow/    # If/else, loops
│   ├── 04_functions/       # Functions, recursion
│   ├── 05_data_structures/ # Lists, tuples, sets, dictionaries
│   ├── 06_strings/         # String operations
│   ├── 07_file_handling/   # Reading/writing files
│   ├── 08_oop/             # Object-Oriented Programming
│   ├── 09_error_handling/  # Try/except, exceptions
│   ├── 10_advanced/        # Lambda, modules, decorators
│   ├── 11_projects/        # Fun games to build
│   └── 12_web/             # Intro to web development
│
├── fastapi/                # Modern REST APIs with FastAPI
├── rest_api/               # Flask + SQLAlchemy API
├── llm_fundamentals/       # Large Language Models from scratch
│   ├── architecture/       # Build GPT from scratch
│   ├── pre_training/       # Train transformer models
│   ├── fine_tuning/        # Fine-tune LLMs
│   └── weight_loading/     # Load pre-trained weights
│
├── data/                   # Dataset files
├── api_reference/          # API documentation
└── requirements.txt        # Install dependencies
```

---

## 🚀 Quick Start

### 1. Install Python

Download Python 3.10 or higher from [python.org](https://www.python.org/downloads/)

### 2. Clone This Repository

```bash
git clone <your-repo-url>
cd python
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Learning!

**Run your first program:**
```bash
cd basics/01_introduction
python 01_hello_world.py
```

---

## 📚 Learning Path

### Phase 1: Python Basics (Weeks 1-4)

| Week | Folder | What You'll Build |
|------|--------|-------------------|
| 1 | `01_introduction` → `03_control_flow` | Calculator, Number Guesser |
| 2 | `04_functions` → `06_strings` | Text Analyzer, Mad Libs Game |
| 3 | `05_data_structures` → `07_file_handling` | To-Do List, File Organizer |
| 4 | `08_oop` → `09_error_handling` | Bank Account System, Quiz Game |

### Phase 2: Advanced Python (Weeks 5-8)

| Week | Folder | What You'll Build |
|------|--------|-------------------|
| 5 | `10_advanced` | Data Processor, Voice Assistant |
| 6 | `11_projects` | Rock-Paper-Scissors, High Score System |
| 7 | `12_web` → `fastapi/` | Hello Web, Campaign API |
| 8 | `rest_api/` | Travel Destinations API |

### Phase 3: AI & LLMs (Weeks 9-12)

| Week | Folder | What You'll Build |
|------|--------|-------------------|
| 9 | `llm_fundamentals/architecture` | Transformer from Scratch |
| 10 | `llm_fundamentals/pre_training` | Train Your Own Model |
| 11 | `llm_fundamentals/weight_loading` | Load GPT-2 Weights |
| 12 | `llm_fundamentals/fine_tuning` | Fine-tune for Custom Tasks |

---

## 🎯 Example: Run a Complete Program

**Guess the Number Game:**
```bash
cd basics/11_projects
python 01_guess_number.py
```

**FastAPI Server:**
```bash
cd fastapi
uvicorn main:app --reload
# Open: http://127.0.0.1:8000/docs
```

**Flask REST API:**
```bash
cd rest_api
python main.py
# Open: http://127.0.0.1:5000/destinations
```

---

## 📖 How to Use This Repository

### For Complete Beginners

1. **Start at the beginning** — Go to `basics/01_introduction/`
2. **Read the README** in each folder
3. **Run the examples** — Type `python filename.py`
4. **Modify the code** — Change values, break things, learn!
5. **Move to the next folder** when comfortable

### For Intermediate Learners

1. **Jump to any topic** you want to learn
2. **Study the examples** in that folder
3. **Build the projects** in `11_projects/`
4. **Try the Web APIs** in `fastapi/` and `rest_api/`

### For Advanced Developers

1. **Explore LLM architecture** in `llm_fundamentals/`
2. **Build transformer models** from scratch
3. **Fine-tune models** for your use cases

---

## 🛠️ Technologies Used

| Category | Tools |
|----------|-------|
| **Core** | Python 3.10+ |
| **Web APIs** | FastAPI, Flask, SQLAlchemy |
| **Deep Learning** | PyTorch, Transformers |
| **LLM Tools** | LangChain, LlamaIndex, LitGPT |
| **Data** | NumPy, Pandas, Matplotlib |

---

## ❓ FAQ

**Q: I'm getting an error. What do I do?**  
A: Read the error message carefully. 99% of errors tell you exactly what's wrong!

**Q: Do I need to install all dependencies?**  
A: For basics, no. For web APIs and LLMs, yes. Install as needed.

**Q: Can I skip ahead?**  
A: Yes! But we recommend following the order for best results.

**Q: How long does this take?**  
A: 2-3 hours/week = Complete in 3 months. 10 hours/week = 1 month.

---

## 🤝 Contributing

Found a bug? Want to add an example?

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-idea`
3. Make your changes
4. Push: `git push origin feature/your-idea`
5. Open a Pull Request

---

## 📄 License

MIT License — Feel free to use this for learning!

---

<div align="center">

### ⭐ Star this repo if it helped you learn!

**Happy Coding! 🎉**

Made with ❤️ for Python learners

</div>
