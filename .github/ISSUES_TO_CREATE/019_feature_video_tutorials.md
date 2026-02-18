---
title: "FEATURE: Add video tutorial links for visual learners"
labels: ["enhancement", "documentation", "good first issue"]
assignees: []
---

## Feature Description

Add curated video tutorial links alongside each topic for learners who prefer visual/audio learning over reading.

## Current State

Only text-based examples and explanations exist. No video resources.

## Proposed Feature

Embed or link to high-quality video tutorials for each major topic.

## Implementation

### 1. Video Resources README

Create a central index:

```markdown
# 📺 Video Tutorials

Curated video tutorials to complement the written content.

## How to Use

1. Read the topic in the main README
2. Watch the corresponding video
3. Code along with the video
4. Complete the exercises

---

## Basics

### Introduction to Python
- [Python for Beginners - Full Course (Programming with Mosh)](https://www.youtube.com/watch?v=_uQrJ0TkZlc) - 6 hours
- [Python Tutorial for Beginners (Corey Schafer)](https://www.youtube.com/watch?v=YYXdXT2l-Gg) - 2 hours

### Variables and Data Types
- [Python Variables and Data Types (FreeCodeCamp)](https://www.youtube.com/watch?v=Z1Yd7upQsXY) - 30 min
- [Python Data Types Explained (Tech With Tim)](https://www.youtube.com/watch?v=O4q3t3R8KJA) - 15 min

### Control Flow
- [Python If/Else and Loops (Corey Schafer)](https://www.youtube.com/watch?v=6iF8Xb7Z3wQ) - 45 min
- [Python Loops Tutorial (Programming with Mosh)](https://www.youtube.com/watch?v=6iF8Xb7Z3wQ) - 20 min

### Functions
- [Python Functions (FreeCodeCamp)](https://www.youtube.com/watch?v=9Os0o3wzS_I) - 40 min
- [Python Functions Explained (Tech With Tim)](https://www.youtube.com/watch?v=Ns4tHEHh8zA) - 25 min

### Data Structures
- [Python Lists, Tuples, Sets, Dicts (Corey Schafer)](https://www.youtube.com/watch?v=W8KRzm-HUcc) - 1 hour
- [Python Data Structures Complete Guide (FreeCodeCamp)](https://www.youtube.com/watch?v=HdL8xGgCj9A) - 2 hours

### File Handling
- [Python File I/O (Programming with Mosh)](https://www.youtube.com/watch?v=Umqyp1XlNFA) - 30 min
- [Working with Files in Python (Tech With Tim)](https://www.youtube.com/watch?v=Umqyp1XlNFA) - 25 min

### Object-Oriented Programming
- [Python OOP Tutorial (Corey Schafer)](https://www.youtube.com/watch?v=ZDa-Z5JzLYM) - 1.5 hours
- [Object Oriented Programming in Python (FreeCodeCamp)](https://www.youtube.com/watch?v=Ej_02ICOIgs) - 4 hours

### Error Handling
- [Python Exception Handling (Tech With Tim)](https://www.youtube.com/watch?v=NIWwJbo-9_8) - 20 min
- [Try/Except in Python (Programming with Mosh)](https://www.youtube.com/watch?v=NIWwJbo-9_8) - 15 min

---

## Web APIs

### FastAPI
- [FastAPI Full Course (FreeCodeCamp)](https://www.youtube.com/watch?v=0sOvCWFmrtA) - 3 hours
- [FastAPI Tutorial (Tech With Tim)](https://www.youtube.com/watch?v=0sOvCWFmrtA) - 1 hour

### Flask
- [Flask Tutorial (Corey Schafer)](https://www.youtube.com/watch?v=MwZwr5Tvyxo) - 2 hours
- [Flask for Beginners (FreeCodeCamp)](https://www.youtube.com/watch?v=Z1RJMH_OqeA) - 4 hours

---

## LLM Fundamentals

### Transformers
- [Transformer Neural Networks (StatQuest)](https://www.youtube.com/watch?v=wjZofJX0v4M) - 30 min
- [Attention Is All You Need Explained (Arxiv Insights)](https://www.youtube.com/watch?v=uQr56M7j410) - 20 min

### Fine-tuning
- [Fine-tuning LLMs (FreeCodeCamp)](https://www.youtube.com/watch?v=HJHmM2hQDhE) - 2 hours
- [LLM Fine-tuning Guide (Weights & Biases)](https://www.youtube.com/watch?v=HJHmM2hQDhE) - 45 min
```

### 2. Embed in Topic READMEs

Add video section to each topic's README:

```markdown
# Topic: Variables and Data Types

## 📚 Written Tutorial
[Link to main content]

## 📺 Video Tutorials

### Quick Overview (10 min)
[Python Variables - Quick Tutorial](link)

### Deep Dive (45 min)
[Complete Variables Guide](link)

### Practice Along (30 min)
[Code Along: Variables](link)

## 📝 After Watching
1. Complete the exercises in this folder
2. Try the coding challenges
3. Build a mini-project using variables
```

### 3. Video Categories

Organize videos by:

**Length:**
- Quick (< 15 min)
- Standard (15-45 min)
- Deep Dive (> 45 min)
- Full Course (> 2 hours)

**Style:**
- Lecture-style
- Code-along
- Project-based
- Concept explanation

**Level:**
- Beginner
- Intermediate
- Advanced

## Quality Criteria for Videos

Only include videos that:
- ✅ Are from reputable creators
- ✅ Have good audio/video quality
- ✅ Are recent (last 3 years for Python, last 1 year for LLMs)
- ✅ Include practical examples
- ✅ Have positive community feedback
- ✅ Match our teaching approach

## Recommended Channels

- Corey Schafer
- FreeCodeCamp
- Programming with Mosh
- Tech With Tim
- ArjanCodes
- StatQuest
- Sentdex
- Keith Galli

## Files to Create

- [ ] `VIDEO_TUTORIALS.md` (main index)
- [ ] Update each topic README with video section
- [ ] Create `quizzes/` for video comprehension (optional)

## Maintenance

- Review links quarterly for broken URLs
- Add new high-quality videos
- Remove outdated content
- Track most-watched videos

## Benefits

- ✅ Caters to different learning styles
- ✅ Visual demonstrations
- ✅ Audio explanations
- ✅ Code-along practice
- ✅ More engaging for some learners
