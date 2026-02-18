---
title: "DOCUMENTATION: Add usage examples to API READMEs"
labels: ["documentation", "good first issue"]
assignees: []
---

## Documentation Issue

The API README files (`api_reference/README.md`, `fastapi/`, `rest_api/`) lack practical, copy-paste-ready examples that learners can use immediately.

## Current State

The READMEs describe endpoints but don't provide enough real-world examples:

```markdown
### Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/campaigns` | List all campaigns |
```

## Expected Content

### For FastAPI (`fastapi/README.md`)

Add complete examples section:

```markdown
## 📝 Usage Examples

### Create a Campaign

**Request:**
```bash
curl -X POST "http://127.0.0.1:8000/campaigns" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Summer Sale 2026",
    "due_date": "2026-08-15T00:00:00"
  }'
```

**Response:**
```json
{
  "campaign_id": 3,
  "name": "Summer Sale 2026",
  "due_date": "2026-08-15T00:00:00",
  "created_at": "2026-02-19T10:30:00"
}
```

### Get All Campaigns

**Request:**
```bash
curl "http://127.0.0.1:8000/campaigns"
```

**Response:**
```json
[
  {
    "campaign_id": 1,
    "name": "Summer Launch",
    "due_date": "2026-06-15T00:00:00",
    "created_at": "2026-02-19T09:00:00"
  },
  {
    "campaign_id": 2,
    "name": "Black Friday",
    "due_date": "2026-11-25T00:00:00",
    "created_at": "2026-02-19T09:00:00"
  }
]
```

### Update a Campaign

**Request:**
```bash
curl -X PUT "http://127.0.0.1:8000/campaigns/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Summer Launch"
  }'
```

### Delete a Campaign

**Request:**
```bash
curl -X DELETE "http://127.0.0.1:8000/campaigns/1"
```

**Response:** `204 No Content`

### Python Client Example

```python
import requests
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000"

# Create a campaign
campaign_data = {
    "name": "Winter Sale",
    "due_date": datetime(2026, 12, 25).isoformat()
}

response = requests.post(f"{BASE_URL}/campaigns", json=campaign_data)
print(response.json())

# Get all campaigns
response = requests.get(f"{BASE_URL}/campaigns")
for campaign in response.json():
    print(f"- {campaign['name']}: {campaign['due_date']}")
```

### JavaScript Client Example

```javascript
const BASE_URL = 'http://127.0.0.1:8000';

// Create a campaign
async function createCampaign(name, dueDate) {
  const response = await fetch(`${BASE_URL}/campaigns`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, due_date: dueDate })
  });
  return await response.json();
}

// Get all campaigns
async function getCampaigns() {
  const response = await fetch(`${BASE_URL}/campaigns`);
  return await response.json();
}
```
```

### For Flask REST API (`rest_api/README.md`)

Similar comprehensive examples for:
- CRUD operations with curl
- Python client using requests
- Error handling examples
- Database seeding examples

## Files to Modify

- [ ] `fastapi/README.md` (add examples section)
- [ ] `rest_api/README.md` (add examples section)
- [ ] `api_reference/README.md` (link to detailed docs)

## Benefits

- ✅ Learners can copy-paste and learn faster
- ✅ Reduces support questions
- ✅ Shows real-world usage
- ✅ Multiple language examples (bash, Python, JS)
