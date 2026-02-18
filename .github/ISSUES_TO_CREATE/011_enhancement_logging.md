---
title: "ENHANCEMENT: Add proper logging throughout the codebase"
labels: ["enhancement", "logging", "intermediate"]
assignees: []
---

## Enhancement Description

The codebase uses `print()` statements for debugging and output instead of proper logging. This makes it difficult to:
- Track errors in production
- Debug issues
- Monitor application health
- Separate debug/info/error messages

## Current State

Examples of print statements throughout the codebase:

```python
# basics/09_error_handling/01_try_except.py
print(f"\nOutput: {round(a, 2)}")
print("A Number Can't be Divide by Zero")

# fastapi/main.py
# No logging at all

# rest_api/main.py
# No logging at all
```

## Problems with print()

- No log levels (INFO, DEBUG, ERROR, etc.)
- No timestamps
- No source information
- Cannot be filtered or configured
- Not suitable for production

## Solution: Python Logging Module

Replace print statements with proper logging.

## Implementation

### 1. Create Logging Configuration

```python
# logging_config.py
import logging
import sys
from pathlib import Path

def setup_logging(name: str, log_file: str = None, level: int = logging.INFO):
    """Configure logging for the application."""
    
    # Create logs directory
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    # File handler (optional)
    handlers = [console_handler]
    if log_file:
        file_handler = logging.FileHandler(log_dir / log_file)
        file_handler.setFormatter(formatter)
        handlers.append(file_handler)
    
    # Configure logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    for handler in handlers:
        logger.addHandler(handler)
    
    return logger
```

### 2. Update Examples

#### Before (basics/09_error_handling/01_try_except.py):
```python
def sum(a: int, b: int) -> int:
    result = a / b
    return result

try:
    a = int(input("Enter the Number: "))
    b = int(input("Enter the Number: "))
    a = sum(a, b)
    print(f"\nOutput: {round(a, 2)}")
except ZeroDivisionError:
    print("A Number Can't be Divide by Zero")
except ValueError:
    print("Enter a Valid Number!")
except Exception as e:
    print(e)
```

#### After:
```python
import logging
logger = logging.getLogger(__name__)

def divide(a: int, b: int) -> float:
    logger.debug(f"Dividing {a} by {b}")
    result = a / b
    logger.debug(f"Result: {result}")
    return result

try:
    a = int(input("Enter the Number: "))
    b = int(input("Enter the Number: "))
    logger.info(f"User input: a={a}, b={b}")
    result = divide(a, b)
    logger.info(f"Output: {round(result, 2)}")
except ZeroDivisionError as e:
    logger.error("Division by zero attempted", exc_info=True)
except ValueError as e:
    logger.warning(f"Invalid input: {e}")
except Exception as e:
    logger.exception(f"Unexpected error: {e}")
```

### 3. Update FastAPI Application

```python
# fastapi/main.py
import logging
from logging_config import setup_logging

logger = setup_logging("campaign_api", "campaign_api.log")

@app.post("/campaigns")
async def create_campaign(campaign: CampaignCreate):
    logger.info(f"Creating campaign: {campaign.name}")
    try:
        # ... create campaign
        logger.info(f"Campaign created with ID: {new_campaign.campaign_id}")
        return new_campaign
    except Exception as e:
        logger.error(f"Failed to create campaign: {e}", exc_info=True)
        raise
```

### 4. Update Flask Application

```python
# rest_api/main.py
import logging
from logging_config import setup_logging

logger = setup_logging("travel_api", "travel_api.log")

@app.route("/destinations", methods=["POST"])
def add_destination():
    logger.info("Adding new destination")
    try:
        data = request.get_json()
        logger.debug(f"Destination data: {data}")
        # ... add destination
        logger.info(f"Destination added: {new_destination.destination}")
        return jsonify(new_destination.to_dict()), 201
    except Exception as e:
        logger.error(f"Failed to add destination: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500
```

## Log Levels Guide

| Level | When to Use | Example |
|-------|-------------|---------|
| DEBUG | Detailed debugging info | Function inputs/outputs |
| INFO | Normal operations | "User logged in" |
| WARNING | Unexpected but handled | "Retry attempt 2/3" |
| ERROR | Error but app continues | "Database connection failed" |
| CRITICAL | Severe error, app may crash | "Out of memory" |

## Files to Create/Modify

- [ ] `logging_config.py` (create - shared logging setup)
- [ ] `basics/09_error_handling/01_try_except.py` (update)
- [ ] `fastapi/main.py` (update)
- [ ] `rest_api/main.py` (update)
- [ ] `llm_fundamentals/**/*.py` (update)
- [ ] `.gitignore` (add `logs/`)

## Documentation

Add logging section to CONTRIBUTING.md:
```markdown
## Logging Guidelines

- Use `logging` module, not `print()`
- Choose appropriate log levels
- Include context in log messages
- Log exceptions with `exc_info=True`
```

## Benefits

- ✅ Production-ready logging
- ✅ Easier debugging
- ✅ Better monitoring
- ✅ Audit trail
- ✅ Teaches best practices
