# 🐍 Python Mastery — From Zero to Hero

> Learn Python the fun way — with hands-on examples, real projects, and zero confusion!

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20APIs-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-AI%20Concepts-purple?style=for-the-badge)
![Beginner Friendly](https://img.shields.io/badge/Beginner-Friendly-orange?style=for-the-badge)

---

## 📖 About

This repository is your **one-stop Python learning hub** — from complete beginner to advanced developer. Learn by reading small explanations and running lots of code.

> 💡 **Philosophy:** Learn by doing. Every concept comes with examples you can run, break, and fix.

---

## 📁 Project Structure

```
Python/
├── Basics/                    # Python fundamentals (112 files, organized)
│   ├── 01_introduction/       # First programs
│   ├── 02_variables_types/    # Variables, operators
│   ├── 03_control_flow/       # Conditions, loops
│   ├── 04_functions/          # Functions, recursion
│   ├── 05_data_structures/    # Lists, tuples, sets, dicts
│   ├── 06_strings/            # String operations
│   ├── 07_file_handling/      # File I/O
│   ├── 08_oop/                # Classes, inheritance
│   ├── 09_error_handling/     # Exceptions
│   ├── 10_advanced/           # Lambda, modules
│   ├── 11_projects/           # Games
│   └── 12_web/                # Flask
├── FastAPI/                   # FastAPI REST API
├── RESTAPI/                   # Flask + SQLAlchemy API
├── LLM(Basics)/               # Large Language Models
│   ├── Architecture/          # Transformer from scratch
│   ├── PRE-TRAINING/          # Model training
│   ├── WEIGHT-LOADING/        # Load GPT-2 weights
│   └── FINE-TUNING/           # Fine-tuning
├── APIs/                      # API documentation
├── CONTRIBUTING.md            # Contribution guide
└── README.md                  # This file
```

---

## 🗂️ Topics Covered

### 🟢 Basics (112 Files in 12 Folders)

| Folder | Topic | Files |
|--------|-------|-------|
| `01_introduction/` | Hello World, Input/Output | 2 |
| `02_variables_types/` | Variables, Types, Operators | 13 |
| `03_control_flow/` | If-Else, Loops, Patterns | 10 |
| `04_functions/` | Functions, Recursion | 11 |
| `05_data_structures/` | List, Tuple, Set, Dict | 20 |
| `06_strings/` | String Operations | 9 |
| `07_file_handling/` | File I/O | 14 |
| `08_oop/` | Classes, Inheritance | 15 |
| `09_error_handling/` | Exceptions | 3 |
| `10_advanced/` | Lambda, Modules | 11 |
| `11_projects/` | Games | 3 |
| `12_web/` | Flask | 1 |

### 🚀 Web APIs
| Framework | File | Description |
|-----------|------|-------------|
| FastAPI | `FastAPI/main.py` | Campaign management API |
| Flask | `RESTAPI/main.py` | Travel destinations CRUD API |

### 🤖 LLM / AI
| Module | Description |
|--------|-------------|
| Architecture | Build GPT from scratch with PyTorch |
| Pre-training | Train transformer models |
| Weight Loading | Load pre-trained GPT-2 weights |
| Fine-tuning | Fine-tune with LitGPT & Qwen |

---

## 🚀 Quick Start

### Prerequisites
```bash
python --version  # Python 3.10+
pip --version
```

### Install Dependencies
```bash
pip install -r requirement.txt
```

### Run Examples

**Basics (Organized by Topic):**
```bash
cd Basics

# Start from the beginning
cd 01_introduction && python hello_world_first.py

# Learn variables
cd ../02_variables_types && python arithmetic_addition.py

# Practice loops
cd ../03_control_flow && python loops_for_while.py

# Build a game
cd ../11_projects && python game_guess_number.py
```

**FastAPI:**
```bash
cd FastAPI
uvicorn main:app --reload
# Visit: http://127.0.0.1:8000
```

**Flask REST API:**
```bash
cd RESTAPI
python main.py
# Visit: http://127.0.0.1:5000/destinations
```

**LLM Training:**
```bash
cd LLM\(Basics\)/PRE-TRAINING
python main.py
```

---

## 📚 Learning Path

### Level 1: Beginner (Weeks 1-2)
1. `01_introduction/` — Hello World, Input
2. `02_variables_types/` — Variables, Operators
3. `03_control_flow/` — Conditions, Loops
4. `04_functions/` — Functions Basics

### Level 2: Intermediate (Weeks 3-4)
1. `05_data_structures/` — Lists, Tuples, Sets, Dicts
2. `06_strings/` — String Operations
3. `07_file_handling/` — File I/O
4. `09_error_handling/` — Exceptions

### Level 3: Advanced (Weeks 5-6)
1. `08_oop/` — Classes, Inheritance
2. `10_advanced/` — Lambda, Map/Filter/Reduce
3. `12_web/` — Flask Basics
4. `11_projects/` — Build Games

### Level 4: Expert
1. Transformer Architecture
2. Pre-training Models
3. Fine-tuning LLMs
4. Weight Loading & Transfer Learning

---

## 🛠️ Technologies

| Category | Tools |
|----------|-------|
| **Language** | Python 3.10+ |
| **Web Frameworks** | FastAPI, Flask |
| **Database** | SQLAlchemy (SQLite) |
| **Deep Learning** | PyTorch, Transformers |
| **LLM Tools** | LangChain, LlamaIndex, LitGPT, Ollama |
| **Visualization** | Matplotlib |
| **Data** | NumPy, Pandas |

---

## 📝 Code Style

This project follows a **beginner-friendly** coding style:
- ✅ Verbose comments explaining each step
- ✅ Print-based output for clarity
- ✅ Type hints where helpful
- ✅ Consistent naming conventions

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit (`git commit -m 'Add feature'`)
5. Push (`git push origin feature/your-feature`)
6. Open a Pull Request

---

## 📖 Resources

| Resource | Link |
|----------|------|
| Python Docs | https://docs.python.org/ |
| FastAPI Docs | https://fastapi.tiangolo.com/ |
| PyTorch | https://pytorch.org/ |
| Hugging Face | https://huggingface.co/ |
| Real Python | https://realpython.com/ |

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

**⭐ Star this repo if it helped you!**

Made with ❤️ for Python learners everywhere.

</div>
