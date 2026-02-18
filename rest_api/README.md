# 🧪 REST API with Flask + SQLAlchemy

Build a complete REST API with database integration.

## What You'll Build

A Travel Destinations API with full CRUD operations:
- ✅ Create destinations
- ✅ Read/List destinations
- ✅ Update destinations
- ✅ Delete destinations

## Run the Server

```bash
python main.py
```

## Access the API

- **Base URL:** http://127.0.0.1:5000
- **Destinations:** http://127.0.0.1:5000/destinations

## Test Endpoints

### Get All Destinations
```bash
curl http://127.0.0.1:5000/destinations
```

### Add Destination
```bash
curl -X POST http://127.0.0.1:5000/destinations \
  -H "Content-Type: application/json" \
  -d '{"destination": "Paris", "country": "France", "rating": 4.8}'
```

### Update Destination
```bash
curl -X PUT http://127.0.0.1:5000/destinations/1 \
  -H "Content-Type: application/json" \
  -d '{"rating": 5.0}'
```

### Delete Destination
```bash
curl -X DELETE http://127.0.0.1:5000/destinations/1
```

## Features

- **SQLAlchemy ORM** - Database abstraction
- **SQLite** - Lightweight database
- **Flask** - Micro web framework
- **RESTful** - Standard HTTP methods

## Next Steps

→ Explore [`llm_fundamentals/`](../llm_fundamentals/) for AI!
