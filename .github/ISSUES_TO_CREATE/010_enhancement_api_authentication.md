---
title: "ENHANCEMENT: Add authentication to FastAPI and Flask APIs"
labels: ["enhancement", "security", "advanced"]
assignees: []
---

## Enhancement Description

Both REST APIs (FastAPI and Flask) currently have no authentication or authorization. Anyone can create, update, or delete data. Adding authentication is essential for production applications and teaches important security concepts.

## Current State

### FastAPI (`fastapi/main.py`)
- All endpoints are public
- No user authentication
- No rate limiting
- No API keys

### Flask (`rest_api/main.py`)
- All endpoints are public
- No user authentication
- No rate limiting

## Security Risks

- Anyone can delete all data
- No audit trail of who did what
- Vulnerable to abuse and attacks
- Not production-ready

## Solution

Implement JWT-based authentication for both APIs.

## Implementation Plan

### Phase 1: FastAPI Authentication

#### 1. Add Dependencies
```
fastapi==0.128.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.21
```

#### 2. Create Auth Module

```python
# fastapi/auth.py
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "your-secret-key"  # Use environment variable in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Validate token and return user
    ...
```

#### 3. Protect Endpoints

```python
@app.post("/campaigns", response_model=Campaign)
async def create_campaign(
    campaign: CampaignCreate,
    current_user: User = Depends(get_current_user)  # Add auth
):
    ...
```

#### 4. Add Auth Endpoints

```python
@app.post("/register")
async def register(username: str, password: str):
    # Create new user

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Return JWT token
```

### Phase 2: Flask Authentication

Similar implementation using:
- `PyJWT` for JWT tokens
- `bcrypt` for password hashing
- `flask-jwt-extended` for easier integration

### Phase 3: Additional Security Features

1. **Rate Limiting**
   ```python
   from slowapi import Limiter
   from slowapi.util import get_remote_address
   
   limiter = Limiter(key_func=get_remote_address)
   
   @app.post("/campaigns")
   @limiter.limit("10/minute")
   async def create_campaign(...):
   ```

2. **API Keys** (alternative to JWT)
   ```python
   class APIKey(BaseModel):
       key: str
       owner: str
   ```

3. **Environment Variables**
   ```python
   import os
   SECRET_KEY = os.environ.get("SECRET_KEY")
   ```

## Files to Create/Modify

### FastAPI
- [ ] `fastapi/auth.py` (create)
- [ ] `fastapi/models.py` (create - User model)
- [ ] `fastapi/main.py` (update with auth)
- [ ] `fastapi/.env.example` (create)

### Flask
- [ ] `rest_api/auth.py` (create)
- [ ] `rest_api/models.py` (update - add User)
- [ ] `rest_api/main.py` (update with auth)

## Documentation

Update API READMEs with:
- How to register
- How to authenticate
- How to use protected endpoints
- Security best practices

## Testing

```bash
# Register
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"password123"}'

# Login
curl -X POST http://localhost:8000/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test&password=password123"

# Use protected endpoint
curl http://localhost:8000/campaigns \
  -H "Authorization: Bearer <token>"
```

## Benefits

- ✅ Production-ready security
- ✅ User management
- ✅ Audit trail capability
- ✅ Rate limiting protection
- ✅ Teaches security best practices
