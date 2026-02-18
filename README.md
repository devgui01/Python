# Python Learning Repository

A collection of Python examples and exercises, from basics to advanced topics like LLMs and web APIs.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Beginner](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## What's Covered

| Level | Topics |
|-------|--------|
| **Beginner** | Variables, Data Types, Operators, Input/Output |
| **Intermediate** | Control Flow, Functions, Data Structures, File Handling |
| **Advanced** | OOP, Error Handling, Modules, Lambda Functions |
| **Expert** | Web APIs (FastAPI, Flask), LLM Architecture, Fine-tuning |

---

## Project Structure

```
python-learning/
├── basics/                 # Python fundamentals - start here
│   ├── 01_introduction/    # Hello World, user input
│   ├── 02_variables_types/ # Variables, operators, type conversion
│   ├── 03_control_flow/    # If/else, loops, patterns
│   ├── 04_functions/       # Functions, recursion
│   ├── 05_data_structures/ # Lists, tuples, sets, dictionaries
│   ├── 06_strings/         # String operations
│   ├── 07_file_handling/   # File I/O
│   ├── 08_oop/             # Object-Oriented Programming
│   ├── 09_error_handling/  # Exceptions, try/except
│   ├── 10_advanced/        # Lambda, modules, decorators
│   ├── 11_projects/        # Games to build
│   └── 12_web/             # Flask introduction
│
├── fastapi/                # REST APIs with FastAPI
├── rest_api/               # Flask + SQLAlchemy APIs
├── llm_fundamentals/       # Build LLMs from scratch
│   ├── architecture/       # Transformer implementation
│   ├── pre_training/       # Model training
│   ├── fine_tuning/        # Fine-tuning techniques
│   └── weight_loading/     # Load pre-trained models
│
├── data/                   # Datasets
└── requirements.txt        # Dependencies
```

---

## Getting Started

### 1. Install Python

Download Python 3.10 or higher from [python.org](https://www.python.org/downloads/)

### 2. Clone the Repository

```bash
git clone <your-repo-url>
cd python
```

### 3. Install Dependencies (Optional)

For basics, no installation needed. For web APIs and LLMs:

```bash
pip install -r requirements.txt
```

### 4. Run Your First Program

```bash
cd basics/01_introduction
python 01_hello_world.py
```

---

## Suggested Learning Path

### Phase 1: Python Basics (Weeks 1-4)

| Week | Folder | Practice Projects |
|------|--------|-------------------|
| 1 | `01_introduction` → `03_control_flow` | Calculator, Number Guesser |
| 2 | `04_functions` → `06_strings` | Text Analyzer, Mad Libs |
| 3 | `05_data_structures` → `07_file_handling` | To-Do List, File Organizer |
| 4 | `08_oop` → `09_error_handling` | Bank Account System, Quiz |

### Phase 2: Advanced Python (Weeks 5-8)

| Week | Folder | Practice Projects |
|------|--------|-------------------|
| 5 | `10_advanced` | Data Processor, Voice Assistant |
| 6 | `11_projects` | Rock-Paper-Scissors, High Score System |
| 7 | `12_web` → `fastapi/` | Hello Web, Campaign API |
| 8 | `rest_api/` | Travel Destinations API |

### Phase 3: AI & LLMs (Weeks 9-12)

| Week | Folder | Practice Projects |
|------|--------|-------------------|
| 9 | `llm_fundamentals/architecture` | Transformer from Scratch |
| 10 | `llm_fundamentals/pre_training` | Train Your Own Model |
| 11 | `llm_fundamentals/weight_loading` | Load GPT-2 Weights |
| 12 | `llm_fundamentals/fine_tuning` | Fine-tune for Custom Tasks |

---

## Running Examples

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

## How to Use This Repository

### If You're New to Python

1. Start at `basics/01_introduction/`
2. Read the README in each folder
3. Run the examples and modify them
4. Move to the next folder when ready

### If You Have Some Experience

1. Jump to any topic you want to learn
2. Study the examples
3. Build the projects in `11_projects/`
4. Try the Web APIs

### If You're Experienced

1. Explore LLM architecture in `llm_fundamentals/`
2. Build transformer models from scratch
3. Fine-tune models for your use cases

---

## Technologies Used

| Category | Tools |
|----------|-------|
| **Core** | Python 3.10+ |
| **Web APIs** | FastAPI, Flask, SQLAlchemy |
| **Deep Learning** | PyTorch, Transformers |
| **LLM Tools** | LangChain, LlamaIndex, LitGPT |
| **Data** | NumPy, Pandas, Matplotlib |

---

## FAQ

**Q: I'm getting an error. What do I do?**  
A: Read the error message carefully - it usually tells you what's wrong.

**Q: Do I need to install all dependencies?**  
A: For basics, no. For web APIs and LLMs, yes. Install as needed.

**Q: Can I skip ahead?**  
A: Yes, but following the order works best.

**Q: How long does this take?**  
A: 2-3 hours/week = 3 months. 10 hours/week = 1 month.

---

## Contributing

Found a bug or want to add an example?

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-idea`
3. Make your changes
4. Push: `git push origin feature/your-idea`
5. Open a Pull Request

---

## License

MIT License

---

<div align="center">

### ⭐ Star this repo if it helped you learn!

**Happy Coding! 🎉**

</div>
