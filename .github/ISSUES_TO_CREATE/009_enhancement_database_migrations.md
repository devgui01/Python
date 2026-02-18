---
title: "ENHANCEMENT: Add database migrations for Flask REST API"
labels: ["enhancement", "database", "intermediate"]
assignees: []
---

## Enhancement Description

The Flask REST API in `rest_api/main.py` uses SQLAlchemy but lacks database migration support. This makes schema changes difficult and is not a best practice for production applications.

## Current State

```python
with app.app_context():
    db.create_all()  # Creates tables, but can't handle changes
```

Problems with current approach:
- Cannot modify existing tables without losing data
- No version control for database schema
- No rollback capability
- Not suitable for production

## Solution: Flask-Migrate (Alembic)

Add database migration support using Flask-Migrate.

## Implementation

### 1. Add Dependencies

Update `requirement.txt`:
```
Flask-Migrate==4.0.5
alembic==1.13.0
```

### 2. Update Flask Application

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Add this

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Add this

class Destination(db.Model):
    # ... existing code ...

# Remove db.create_all() - migrations handle this now

# Add CLI command for migrations
@app.cli.command()
def init_db():
    """Initialize the database."""
    from flask_migrate import upgrade
    db.create_all()
    print("Database initialized!")
```

### 3. Migration Commands

```bash
# Initialize migrations (run once)
flask db init

# Create a new migration
flask db migrate -m "Initial migration"

# Apply migrations
flask db upgrade

# Rollback
flask db downgrade -1
```

### 4. Example Migration Scenario

When adding a new field:

```python
# Update model
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)  # New field!
```

Then run:
```bash
flask db migrate -m "Add description field"
flask db upgrade
```

## Files to Create/Modify

- [ ] `rest_api/requirements.txt` (add Flask-Migrate)
- [ ] `rest_api/main.py` (update with migrations)
- [ ] `rest_api/migrations/` (auto-generated)
- [ ] `rest_api/README.md` (add migration docs)

## Documentation

Add to `rest_api/README.md`:

```markdown
## Database Migrations

### Setup
```bash
pip install Flask-Migrate
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Making Changes
1. Modify your models
2. Run `flask db migrate -m "Description of change"`
3. Run `flask db upgrade`

### Rollback
```bash
flask db downgrade -1
```
```

## Benefits

- ✅ Safe schema changes
- ✅ Data preservation during updates
- ✅ Version control for database
- ✅ Team collaboration
- ✅ Production-ready practice

## Learning Value

Teaches learners:
- Database version control
- Production best practices
- Schema evolution
- Alembic migration tool
