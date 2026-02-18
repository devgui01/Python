# API Examples — FastAPI & Flask

> Build REST APIs with Python

---

## 📁 Structure

```
├── FastAPI/             # Modern, fast API
│   └── main.py          # Campaign management API
└── RESTAPI/             # Flask + SQLAlchemy
    └── main.py          # Travel destinations API
```

---

## 🚀 FastAPI

Modern, fast web framework for building APIs.

### Features
- Automatic docs (`/docs`)
- Type validation
- Async support
- Fast performance

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/campaigns` | List all campaigns |
| GET | `/campaigns/{id}` | Get campaign by ID |

### Run
```bash
cd FastAPI
uvicorn main:app --reload

# Visit:
# http://127.0.0.1:8000
# http://127.0.0.1:8000/docs
```

### Example Request
```bash
curl http://127.0.0.1:8000/campaigns
```

---

## 🌸 Flask REST API

Simple, flexible web framework with SQLAlchemy.

### Features
- SQLite database
- Full CRUD operations
- JSON responses

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/destinations` | List all destinations |
| GET | `/destinations/{id}` | Get destination by ID |
| POST | `/destinations` | Add destination |
| PUT | `/destinations/{id}` | Update destination |
| DELETE | `/destinations/{id}` | Delete destination |

### Run
```bash
cd RESTAPI
python main.py

# Visit: http://127.0.0.1:5000
```

### Example Requests

**Get all destinations:**
```bash
curl http://127.0.0.1:5000/destinations
```

**Add destination:**
```bash
curl -X POST http://127.0.0.1:5000/destinations \
  -H "Content-Type: application/json" \
  -d '{"destination":"Paris","country":"France","rating":4.8}'
```

**Delete destination:**
```bash
curl -X DELETE http://127.0.0.1:5000/destinations/1
```

---

## 📊 Comparison

| Feature | FastAPI | Flask |
|---------|---------|-------|
| Speed | ⚡ Very Fast | 🐢 Moderate |
| Type Validation | ✅ Built-in | ⚠️ Manual |
| Auto Docs | ✅ Yes | ❌ No |
| Learning Curve | 📈 Medium | 📉 Low |
| Best For | Modern APIs | Simple APIs |

---

## 💡 Tips

1. **Use FastAPI** for new projects
2. **Use Flask** for simple, quick APIs
3. **Always test** your endpoints
4. **Use Postman/curl** for testing

---

## 📚 Resources

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Flask Docs](https://flask.palletsprojects.com/)
- [SQLAlchemy Docs](https://www.sqlalchemy.org/)

Happy coding! 🚀
