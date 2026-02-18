# ⚡ FastAPI - Modern REST APIs

Build fast, modern APIs with FastAPI.

## What You'll Build

A complete Campaign Management API with:
- ✅ Create campaigns
- ✅ List all campaigns
- ✅ Get campaign by ID
- ✅ Update campaigns
- ✅ Delete campaigns

## Run the Server

```bash
uvicorn main:app --reload
```

## Access the API

- **API:** http://127.0.0.1:8000
- **Interactive Docs:** http://127.0.0.1:8000/docs
- **Alternative Docs:** http://127.0.0.1:8000/redoc

## Test Endpoints

### Get All Campaigns
```bash
curl http://127.0.0.1:8000/campaigns
```

### Create Campaign
```bash
curl -X POST http://127.0.0.1:8000/campaigns \
  -H "Content-Type: application/json" \
  -d '{"name": "New Campaign", "due_date": "2026-12-31T00:00:00"}'
```

## Features

- **Pydantic Models** - Automatic validation
- **Type Hints** - Better editor support
- **Auto Docs** - Interactive API documentation
- **Fast** - High performance (as fast as NodeJS and Go)

## Next Steps

→ Explore [`rest_api/`](../rest_api/) for Flask + SQLAlchemy!
