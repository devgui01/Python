---
title: "FEATURE: Add quiz system for knowledge checks"
labels: ["enhancement", "feature", "intermediate"]
assignees: []
---

## Feature Description

Add a quiz system that allows learners to test their understanding after completing each topic. Quizzes provide immediate feedback and reinforce learning.

## Current State

No knowledge checks or quizzes exist. Learners complete topics without verifying understanding.

## Proposed Feature

Quiz system with:
- Multiple choice questions
- Code completion questions
- True/False questions
- Immediate feedback
- Score tracking
- Topic-based quizzes

## Implementation

### 1. Quiz Data Structure

```python
# quizzes/data.py
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum

class QuestionType(Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"
    CODE_COMPLETION = "code_completion"
    FILL_BLANK = "fill_blank"

@dataclass
class Question:
    id: str
    question_type: QuestionType
    question_text: str
    options: Optional[List[str]] = None
    correct_answer: str = None
    explanation: str = ""
    difficulty: str = "easy"  # easy, medium, hard
    points: int = 1

@dataclass
class Quiz:
    id: str
    title: str
    topic: str  # e.g., "01_introduction", "02_variables_types"
    questions: List[Question]
    passing_score: float = 70.0  # percentage
```

### 2. Sample Quiz

```python
# quizzes/basics/quiz_01_introduction.py
from data import Quiz, Question, QuestionType

quiz_01 = Quiz(
    id="quiz_01",
    title="Introduction to Python",
    topic="01_introduction",
    passing_score=70.0,
    questions=[
        Question(
            id="q1",
            question_type=QuestionType.MULTIPLE_CHOICE,
            question_text="Which function is used to display output in Python?",
            options=["print()", "echo()", "display()", "write()"],
            correct_answer="print()",
            explanation="print() is the built-in function for output in Python 3",
            difficulty="easy",
            points=1
        ),
        Question(
            id="q2",
            question_type=QuestionType.TRUE_FALSE,
            question_text="Python is a compiled language.",
            correct_answer="False",
            explanation="Python is an interpreted language, though it does compile to bytecode",
            difficulty="easy",
            points=1
        ),
        Question(
            id="q3",
            question_type=QuestionType.CODE_COMPLETION,
            question_text="Complete the code to print 'Hello':\nprint(____)",
            correct_answer="'Hello'",
            explanation="Strings in Python must be enclosed in quotes",
            difficulty="medium",
            points=2
        ),
        Question(
            id="q4",
            question_type=QuestionType.FILL_BLANK,
            question_text="The ___ function is used to get user input.",
            correct_answer="input",
            explanation="input() reads a line from input and returns it as a string",
            difficulty="easy",
            points=1
        ),
    ]
)
```

### 3. Quiz Runner

```python
# quizzes/runner.py
import json
from typing import Dict
from datetime import datetime

class QuizRunner:
    def __init__(self, quiz: Quiz):
        self.quiz = quiz
        self.score = 0
        self.answers = {}
    
    def display_question(self, question: Question, num: int):
        """Display a question to the user."""
        print(f"\n{'='*60}")
        print(f"Question {num}/{len(self.quiz.questions)}")
        print(f"Points: {question.points}")
        print(f"Difficulty: {question.difficulty}")
        print(f"{'='*60}")
        print(f"\n{question.question_text}\n")
        
        if question.question_type == QuestionType.MULTIPLE_CHOICE:
            for i, option in enumerate(question.options, 1):
                print(f"  {i}. {option}")
        elif question.question_type == QuestionType.TRUE_FALSE:
            print("  1. True")
            print("  2. False")
    
    def get_answer(self, question: Question) -> str:
        """Get user's answer."""
        if question.question_type in [QuestionType.MULTIPLE_CHOICE, QuestionType.TRUE_FALSE]:
            while True:
                try:
                    choice = int(input("\nYour answer (number): "))
                    if question.question_type == QuestionType.TRUE_FALSE:
                        return "True" if choice == 1 else "False"
                    return question.options[choice - 1]
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a number.")
        else:
            return input("Your answer: ")
    
    def check_answer(self, question: Question, answer: str) -> bool:
        """Check if answer is correct."""
        is_correct = answer.strip().lower() == question.correct_answer.strip().lower()
        
        if is_correct:
            self.score += question.points
            print("\n✅ Correct!")
        else:
            print(f"\n❌ Incorrect. The correct answer was: {question.correct_answer}")
        
        if question.explanation:
            print(f"\n💡 Explanation: {question.explanation}")
        
        return is_correct
    
    def run_quiz(self):
        """Run the complete quiz."""
        print(f"\n📝 Starting Quiz: {self.quiz.title}")
        print(f"Passing Score: {self.quiz.passing_score}%")
        print(f"Total Questions: {len(self.quiz.questions)}")
        
        for i, question in enumerate(self.quiz.questions, 1):
            self.display_question(question, i)
            answer = self.get_answer(question)
            self.answers[question.id] = answer
            self.check_answer(question, answer)
        
        self.show_results()
    
    def show_results(self):
        """Display quiz results."""
        total_points = sum(q.points for q in self.quiz.questions)
        percentage = (self.score / total_points) * 100
        
        print(f"\n{'='*60}")
        print("📊 Quiz Results")
        print(f"{'='*60}")
        print(f"Score: {self.score}/{total_points} ({percentage:.1f}%)")
        print(f"Passing Score: {self.quiz.passing_score}%")
        
        if percentage >= self.quiz.passing_score:
            print("\n🎉 Congratulations! You passed!")
        else:
            print("\n📚 Keep studying! You can try again.")
        
        print(f"{'='*60}\n")
```

### 4. CLI Interface

```python
# scripts/quiz.py
import sys
import importlib.util

def load_quiz(quiz_file: str):
    spec = importlib.util.spec_from_file_location("quiz_module", quiz_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.quiz_01  # Adjust based on actual variable name

def main():
    if len(sys.argv) < 2:
        print("Usage: python quiz.py <quiz_number>")
        print("Example: python quiz.py 01")
        sys.exit(1)
    
    quiz_num = sys.argv[1]
    quiz_file = f"quizzes/basics/quiz_{quiz_num}_introduction.py"
    
    try:
        quiz = load_quiz(quiz_file)
        runner = QuizRunner(quiz)
        runner.run_quiz()
    except FileNotFoundError:
        print(f"Quiz {quiz_num} not found!")
        sys.exit(1)
```

### 5. Quiz Topics

Create quizzes for:

**Basics:**
- [ ] Quiz 01: Introduction
- [ ] Quiz 02: Variables & Types
- [ ] Quiz 03: Control Flow
- [ ] Quiz 04: Functions
- [ ] Quiz 05: Data Structures
- [ ] Quiz 06: Strings
- [ ] Quiz 07: File Handling
- [ ] Quiz 08: OOP
- [ ] Quiz 09: Error Handling
- [ ] Quiz 10: Advanced Topics

**Web APIs:**
- [ ] Quiz: FastAPI Basics
- [ ] Quiz: Flask Basics
- [ ] Quiz: REST Principles

**LLM:**
- [ ] Quiz: Transformer Architecture
- [ ] Quiz: Pre-training
- [ ] Quiz: Fine-tuning

### 6. Progress Tracking

```python
# quizzes/progress.py
import json
from pathlib import Path
from datetime import datetime

class QuizProgress:
    def __init__(self):
        self.file = Path(".quiz_progress.json")
        self.data = self.load()
    
    def record_quiz_attempt(self, quiz_id: str, score: float, passed: bool):
        if quiz_id not in self.data:
            self.data[quiz_id] = []
        
        self.data[quiz_id].append({
            "date": datetime.now().isoformat(),
            "score": score,
            "passed": passed
        })
        self.save()
    
    def get_best_score(self, quiz_id: str) -> float:
        attempts = self.data.get(quiz_id, [])
        if not attempts:
            return 0.0
        return max(a["score"] for a in attempts)
    
    def get_summary(self) -> dict:
        total = len(self.data)
        passed = sum(1 for quiz_id in self.data if self.get_best_score(quiz_id) >= 70)
        return {"total_quizzes": total, "passed": passed}
```

## Files to Create

- [ ] `quizzes/data.py`
- [ ] `quizzes/runner.py`
- [ ] `quizzes/progress.py`
- [ ] `quizzes/basics/` (quiz definitions)
- [ ] `scripts/quiz.py`
- [ ] `quizzes/README.md`

## Usage

```bash
# Take a quiz
python scripts/quiz.py 01

# View progress
python scripts/quiz_progress.py
```

## Benefits

- ✅ Reinforces learning
- ✅ Identifies knowledge gaps
- ✅ Gamification element
- ✅ Track progress
- ✅ Build confidence
