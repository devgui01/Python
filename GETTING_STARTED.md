# 🚀 Get Started with Python Learning Platform

Your journey from Python beginner to expert starts here!

---

## ⚡ Quick Start (5 minutes)

### Option 1: Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/hackdartstorm/Python.git
cd Python

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install dependencies (optional - for advanced topics)
pip install -r requirements.txt

# 5. Run your first program
cd basics/01_introduction
python 01_hello_world.py
```

### Option 2: Docker (Recommended for consistency)

```bash
# Build and run with Docker Compose
docker-compose up dev

# Run tests
docker-compose up test

# Start FastAPI example
docker-compose up fastapi
```

---

## 📚 Learning Paths

### Path 1: Complete Beginner
**Time:** 8-12 weeks | **Prerequisites:** None

1. **Week 1-2:** Python Basics
   - `basics/01_introduction/` - Hello World
   - `basics/02_variables_types/` - Variables & Data Types
   - `basics/03_control_flow/` - If/Else, Loops

2. **Week 3-4:** Core Concepts
   - `basics/04_functions/` - Functions
   - `basics/05_data_structures/` - Lists, Dicts, Sets
   - `basics/06_strings/` - String Operations

3. **Week 5-6:** Intermediate Topics
   - `basics/07_file_handling/` - File I/O
   - `basics/08_oop/` - Object-Oriented Programming
   - `basics/09_error_handling/` - Exceptions

4. **Week 7-8:** Advanced & Projects
   - `basics/10_advanced/` - Lambda, Modules
   - `basics/11_projects/` - Build Games
   - Complete 10+ exercises

### Path 2: Web Development
**Time:** 6-8 weeks | **Prerequisites:** Python Basics

1. FastAPI fundamentals
2. Flask web development
3. Database integration
4. Build REST APIs
5. Deploy to production

### Path 3: AI/ML Engineering
**Time:** 12-16 weeks | **Prerequisites:** Intermediate Python

1. `llm_fundamentals/architecture/` - Transformer models
2. `llm_fundamentals/pre_training/` - Training
3. `llm_fundamentals/fine_tuning/` - Fine-tuning
4. Build custom LLM applications

---

## 🎯 What You'll Build

### Beginner Projects
- ✅ Calculator
- ✅ Number Guessing Game
- ✅ To-Do List App
- ✅ Text Analyzer

### Intermediate Projects
- ✅ Weather API Client
- ✅ Expense Tracker
- ✅ Blog Platform
- ✅ File Organizer

### Advanced Projects
- ✅ REST API with Authentication
- ✅ Machine Learning Model
- ✅ Real-time Chat Application
- ✅ E-commerce Backend

---

## 📖 Documentation

| Resource | Description | Link |
|----------|-------------|------|
| **Cheat Sheets** | Quick reference guides | [docs/cheat-sheets/](docs/cheat-sheets/) |
| **Exercises** | 50+ coding challenges | [exercises/](exercises/) |
| **Projects** | Capstone project ideas | [projects/capstone/](projects/capstone/) |
| **Roadmap** | Learning path & goals | [ROADMAP.md](ROADMAP.md) |
| **API Docs** | FastAPI/Flask documentation | Coming soon |

---

## 🛠️ Development Setup

### Install Pre-commit Hooks (Recommended)

```bash
# Install pre-commit
pip install pre-commit

# Set up hooks
pre-commit install

# Run on all files
pre-commit run --all-files
```

### Run Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=. --cov-report=html
```

### Code Formatting

```bash
# Format code
black .

# Lint code
ruff check .

# Sort imports
isort .
```

---

## 📊 Track Your Progress

```bash
# Mark exercise as complete
python tools/progress.py mark 001

# View your progress
python tools/progress.py status

# Validate exercise solution
python tools/validate.py 001
```

---

## 🤝 Getting Help

### Stuck on something?

1. **Check the docs** - Many questions are answered in [docs/](docs/)
2. **Search issues** - Someone might have asked already
3. **Ask in discussions** - GitHub Discussions
4. **Join Discord** - Real-time help from community

### Want to contribute?

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Run tests: `pytest tests/`
5. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📋 Project Structure

```
python-learning/
├── basics/                 # Start here! Python fundamentals
│   ├── 01_introduction/    # Hello World, input/output
│   ├── 02_variables_types/ # Variables, operators
│   ├── 03_control_flow/    # If/else, loops
│   └── ...
├── exercises/              # Coding challenges
│   ├── README.md
│   └── solutions/
├── projects/               # Capstone projects
│   └── capstone/
├── tests/                  # Unit tests
├── tools/                  # Progress tracker, validator
├── docs/                   # Documentation
│   └── cheat-sheets/
├── fastapi/                # FastAPI examples
├── rest_api/               # Flask REST API
├── llm_fundamentals/       # LLM from scratch
├── Dockerfile              # Docker setup
├── docker-compose.yml      # Docker services
├── pyproject.toml          # Project configuration
├── requirements.txt        # Dependencies
└── ROADMAP.md              # Future plans
```

---

## 🎓 Certification Path (Coming Soon)

Complete specific tracks to earn certificates:

| Certificate | Requirements | Status |
|-------------|--------------|--------|
| Python Basics | Complete 01-09 + 20 exercises | ✅ Available |
| Web Developer | FastAPI + Flask + Database | 🚧 In Progress |
| Data Scientist | NumPy + Pandas + Visualization | 📋 Planned |
| ML Engineer | LLM Fundamentals + Projects | 📋 Planned |

---

## 📈 Success Stories

> "This repository helped me land my first Python developer job!" - @developer123

> "The capstone projects were perfect for my portfolio." - @coder456

**Want to share your story?** Open a discussion!

---

## 🔗 Additional Resources

### Books
- "Python Crash Course" by Eric Matthes
- "Fluent Python" by Luciano Ramalho
- "Automate the Boring Stuff" by Al Sweigart

### Websites
- [Python.org](https://python.org) - Official documentation
- [Real Python](https://realpython.com) - Tutorials
- [LeetCode](https://leetcode.com) - Practice problems

### YouTube Channels
- Core Python Programming
- Tech With Tim
- FreeCodeCamp

---

## ❓ FAQ

**Q: Which Python version should I use?**  
A: Python 3.10 or higher. We test on 3.10, 3.11, and 3.12.

**Q: Do I need to install all dependencies?**  
A: For basics, no. For web APIs and LLMs, yes. Install as needed.

**Q: How long does it take to complete?**  
A: Basics: 8-12 weeks (2-3 hours/week). Full curriculum: 6 months.

**Q: Can I use this for my university course?**  
A: Yes! Many instructors use this as supplementary material.

**Q: Is this really free?**  
A: Yes! Completely free under MIT license.

---

## 🚀 Ready to Start?

```bash
# Your first command
cd basics/01_introduction
python 01_hello_world.py
```

**Happy Coding! 🐍✨**

---

<div align="center">

[Report Bug](https://github.com/hackdartstorm/Python/issues) · [Request Feature](https://github.com/hackdartstorm/Python/issues) · [Discussions](https://github.com/hackdartstorm/Python/discussions)

⭐ **Star this repo if you find it helpful!**

</div>
