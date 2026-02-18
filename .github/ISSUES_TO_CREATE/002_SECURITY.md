# 🔒 SECURITY ISSUES - Priority: HIGH

---

## Issue #6: Flask REST API Has SQL Injection Vulnerability

### Title
[SECURITY]: Flask REST API vulnerable to SQL injection attacks

### Description

**What:** The Flask REST API in `rest_api/main.py` uses string interpolation for database queries, making it vulnerable to SQL injection attacks.

**Why it matters:** Attackers could execute arbitrary SQL commands, potentially accessing, modifying, or deleting all data in the database.

**Where:** `rest_api/main.py`, lines 44-50 (POST endpoint)

**Current behavior:**
```python
@app.route("/destinations", methods=["POST"])
def add_destination():
    data = request.get_json()
    new_destination = Destination(
        destination=data["destination"],  # No validation!
        country=data["country"],          # No validation!
        rating=data["rating"]             # No validation!
    )
```

**Vulnerability:** While SQLAlchemy ORM provides some protection, there's no input validation, length limits, or sanitization. Malicious input could still cause issues.

**Suggested approach:**
1. Add input validation with Flask-WTF or marshmallow
2. Add length constraints
3. Add type validation
4. Sanitize all inputs

```python
from marshmallow import Schema, fields, validate

class DestinationSchema(Schema):
    destination = fields.Str(required=True, validate=validate.Length(max=100))
    country = fields.Str(required=True, validate=validate.Length(max=50))
    rating = fields.Float(required=True, validate=validate.Range(min=0, max=5))
```

**Acceptance criteria:**
- [ ] Add input validation schema
- [ ] Validate all incoming JSON data
- [ ] Add length constraints to all string fields
- [ ] Add range validation for rating (0-5)
- [ ] Return 400 Bad Request for invalid input
- [ ] Add tests for malicious input

**Labels:** `security`, `bug`, `priority: high`

---

## Issue #7: Debug Mode Enabled in Flask Production App

### Title
[SECURITY]: Flask debug mode enabled in production

### Description

**What:** The Flask application runs with `debug=True`, which should never be used in production.

**Why it matters:** Debug mode exposes:
- Interactive debugger (code execution)
- Detailed error messages with stack traces
- Source code disclosure
- Server information

**Where:** `rest_api/main.py`, line 72

**Current behavior:**
```python
if __name__ == "__main__":
    app.run(debug=True)  # DANGEROUS in production!
```

**Suggested approach:**
Use environment variable to control debug mode:

```python
import os

if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug_mode)
```

**Acceptance criteria:**
- [ ] Remove hardcoded `debug=True`
- [ ] Add environment variable configuration
- [ ] Default to `debug=False`
- [ ] Document in README how to enable for development
- [ ] Add warning in comments about production use

**Labels:** `security`, `bug`, `priority: high`

---

## Issue #8: No Input Validation in FastAPI Campaign API

### Title
[SECURITY]: FastAPI campaign endpoint accepts unvalidated future dates

### Description

**What:** The campaign creation endpoint accepts any datetime value, including dates in the past or far future without validation.

**Why it matters:** Business logic error - campaigns could be created with invalid due dates.

**Where:** `fastapi/main.py`, CampaignCreate model (lines 23-26)

**Suggested approach:**
Add custom validator:

```python
from datetime import datetime, timedelta
from pydantic import validator, BaseModel, Field

class CampaignCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    due_date: datetime = Field(..., description="Campaign due date")
    
    @validator('due_date')
    def due_date_must_be_future(cls, v):
        if v < datetime.now():
            raise ValueError('due_date must be in the future')
        if v > datetime.now() + timedelta(days=365*10):
            raise ValueError('due_date cannot be more than 10 years in future')
        return v
```

**Acceptance criteria:**
- [ ] Add max_length validation for name
- [ ] Add validator for future dates only
- [ ] Add reasonable upper bound (e.g., 10 years)
- [ ] Return 422 for invalid dates
- [ ] Add test cases for edge cases

**Labels:** `security`, `enhancement`, `priority: medium`

---

## Issue #9: Hardcoded Model Name in LangChain Example

### Title
[SECURITY]: Hardcoded AI model name without environment variable support

### Description

**What:** The LangChain search example (`basics/10_advanced/11_langchain_search.py`) has a hardcoded model name that may not exist or may cost money to use.

**Why it matters:** 
- Students may accidentally use paid models
- Model may not be available
- No way to configure without editing code

**Where:** `basics/10_advanced/11_langchain_search.py`, line 8

**Current behavior:**
```python
llm = ChatOllama(
    model="Your AI Model",  # Placeholder that doesn't work!
    temperature=0.2
)
```

**Suggested approach:**
Use environment variable with sensible default:

```python
import os

llm = ChatOllama(
    model=os.environ.get("OLLAMA_MODEL", "llama3.2"),
    temperature=0.2
)
```

**Acceptance criteria:**
- [ ] Replace hardcoded model with environment variable
- [ ] Provide free, local model as default (e.g., llama3.2)
- [ ] Add .env.example file
- [ ] Document required environment variables
- [ ] Add warning about API costs

**Labels:** `security`, `enhancement`, `good first issue`

---

## Issue #10: No Rate Limiting on API Endpoints

### Title
[SECURITY]: API endpoints have no rate limiting

### Description

**What:** Both FastAPI and Flask APIs have no rate limiting, making them vulnerable to DoS attacks and abuse.

**Why it matters:** Attackers could:
- Overwhelm the server with requests
- Exhaust database connections
- Consume all server resources

**Where:** 
- `fastapi/main.py` - All endpoints
- `rest_api/main.py` - All endpoints

**Suggested approach:**

For FastAPI:
```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/campaigns")
@limiter.limit("100/minute")
async def list_campaigns(request: Request):
    ...
```

For Flask:
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(app, key_func=get_remote_address)

@app.route("/destinations")
@limiter.limit("100/minute")
def get_destinations():
    ...
```

**Acceptance criteria:**
- [ ] Add rate limiting to FastAPI (100 req/min per IP)
- [ ] Add rate limiting to Flask (100 req/min per IP)
- [ ] Return 429 Too Many Requests when exceeded
- [ ] Document rate limits in API docs
- [ ] Add tests for rate limiting

**Labels:** `security`, `enhancement`, `priority: medium`

---
