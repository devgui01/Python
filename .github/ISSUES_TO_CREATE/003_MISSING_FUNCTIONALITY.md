# 📦 MISSING FUNCTIONALITY - Priority: MEDIUM

---

## Issue #11: FastAPI Uses In-Memory Storage

### Title
[FEATURE]: Add database persistence to FastAPI campaign API

### Description

**What:** The FastAPI campaign API stores data in a Python list, which is lost when the server restarts.

**Why it matters:** 
- Data persistence is essential for real applications
- Students don't learn proper database integration
- No demonstration of ORM patterns

**Where:** `fastapi/main.py`, lines 43-56

**Current behavior:**
```python
campaigns_db: list[Campaign] = [...]  # Lost on restart!
next_campaign_id = 3
```

**Expected behavior:** Data should persist across server restarts using a database.

**Suggested approach:**
Add SQLAlchemy integration:

1. Install: `pip install sqlalchemy databases[sqlite]`
2. Create models.py with Campaign model
3. Create database.py with connection
4. Update main.py to use database

```python
# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./campaigns.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
```

**Acceptance criteria:**
- [ ] Add SQLAlchemy dependency to requirements.txt
- [ ] Create database.py with connection setup
- [ ] Create models.py with Campaign table
- [ ] Update endpoints to use database queries
- [ ] Add database migration/initialization
- [ ] Test data persists after restart

**Labels:** `feature`, `enhancement`, `priority: medium`

---

## Issue #12: No DELETE Cascade in Flask REST API

### Title
[FEATURE]: Add soft delete instead of hard delete for destinations

### Description

**What:** The Flask API permanently deletes records. Production systems typically use soft delete for audit trails.

**Why it matters:** 
- No audit trail of deleted items
- Can't recover accidentally deleted data
- Doesn't demonstrate best practices

**Where:** `rest_api/main.py`, lines 64-70

**Suggested approach:**
Add soft delete with `is_deleted` flag:

```python
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    deleted_at = db.Column(db.DateTime)
    
    def to_dict(self):
        return {
            "id": self.id,
            "destination": self.destination,
            "country": self.country,
            "rating": self.rating,
            "is_deleted": self.is_deleted
        }

@app.route("/destinations/<int:destination_id>", methods=["DELETE"])
def delete_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination:
        destination.is_deleted = True
        destination.deleted_at = datetime.utcnow()
        db.session.commit()
        return jsonify({"message": "Destination was soft-deleted!"})
```

**Acceptance criteria:**
- [ ] Add is_deleted and deleted_at columns
- [ ] Update DELETE to set flags instead of removing
- [ ] Update GET to filter out soft-deleted items
- [ ] Add endpoint to list all (including deleted)
- [ ] Add endpoint to permanently delete (admin only)

**Labels:** `feature`, `enhancement`, `priority: low`

---

## Issue #13: No Pagination in API Endpoints

### Title
[FEATURE]: Add pagination to list endpoints

### Description

**What:** API endpoints return all records at once, which doesn't scale.

**Why it matters:** 
- Performance degrades with large datasets
- Wastes bandwidth
- Doesn't demonstrate best practices

**Where:** 
- `fastapi/main.py` - GET /campaigns
- `rest_api/main.py` - GET /destinations

**Suggested approach:**

For FastAPI:
```python
from fastapi import Query

@app.get("/campaigns", response_model=list[Campaign])
async def list_campaigns(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000)
):
    return campaigns_db[skip:skip + limit]
```

For Flask:
```python
@app.route("/destinations", methods=["GET"])
def get_destinations():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    destinations = Destination.query.paginate(page=page, per_page=per_page)
    return jsonify([d.to_dict() for d in destinations.items])
```

**Acceptance criteria:**
- [ ] Add skip/limit or page/per_page parameters
- [ ] Set reasonable defaults (page=1, per_page=20)
- [ ] Set maximum limits (per_page <= 100)
- [ ] Return pagination metadata (total, pages, has_next)
- [ ] Update API documentation

**Labels:** `feature`, `performance`, `priority: medium`

---

## Issue #14: No Search or Filter Functionality

### Title
[FEATURE]: Add search and filter capabilities to API endpoints

### Description

**What:** APIs have no way to search or filter results.

**Why it matters:** 
- Essential for real-world applications
- Improves user experience
- Demonstrates query parameter handling

**Where:** 
- `fastapi/main.py` - GET /campaigns
- `rest_api/main.py` - GET /destinations

**Suggested approach:**

For FastAPI:
```python
@app.get("/campaigns")
async def list_campaigns(
    search: str = Query(None),
    min_rating: float = Query(None),
    due_before: datetime = Query(None)
):
    results = campaigns_db
    if search:
        results = [c for c in results if search.lower() in c.name.lower()]
    if min_rating:
        results = [c for c in results if c.rating >= min_rating]
    return results
```

**Acceptance criteria:**
- [ ] Add search query parameter
- [ ] Add filter parameters (date range, rating, etc.)
- [ ] Implement case-insensitive search
- [ ] Combine multiple filters with AND logic
- [ ] Document all filter options

**Labels:** `feature`, `enhancement`, `priority: medium`

---

## Issue #15: No Health Check Endpoint

### Title
[FEATURE]: Add health check endpoint for monitoring

### Description

**What:** APIs have no health check endpoint for monitoring and load balancers.

**Why it matters:** 
- Essential for production deployments
- Needed for Kubernetes/Docker health checks
- Helps with monitoring and alerting

**Where:** Both API applications

**Suggested approach:**

For FastAPI:
```python
@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }
```

For Flask:
```python
@app.route("/health")
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    })
```

**Acceptance criteria:**
- [ ] Add /health endpoint to FastAPI
- [ ] Add /health endpoint to Flask
- [ ] Include status, timestamp, version
- [ ] Add database connectivity check
- [ ] Return 200 OK when healthy, 503 when unhealthy

**Labels:** `feature`, `enhancement`, `good first issue`

---

## Issue #16: No API Versioning

### Title
[FEATURE]: Implement API versioning strategy

### Description

**What:** APIs have no versioning, making it impossible to introduce breaking changes.

**Why it matters:** 
- Breaking changes break existing clients
- Industry standard practice
- Needed for long-term maintenance

**Where:** Both API applications

**Suggested approach:**

URL versioning (recommended):
```python
# FastAPI
app = FastAPI(root_path="/api/v1")

# Routes become:
# /api/v1/campaigns
# /api/v1/health
```

Or header versioning:
```python
@app.get("/campaigns")
async def list_campaigns(
    x_api_version: str = Header(default="v1")
):
    if x_api_version == "v2":
        # New behavior
    else:
        # Old behavior
```

**Acceptance criteria:**
- [ ] Choose versioning strategy (URL recommended)
- [ ] Update all route paths
- [ ] Add version to API documentation
- [ ] Document versioning strategy in README
- [ ] Plan for v2 deprecation policy

**Labels:** `feature`, `enhancement`, `priority: low`

---

## Issue #17: No Bulk Operations

### Title
[FEATURE]: Add bulk create/update/delete operations

### Description

**What:** APIs only support single-item operations, not bulk operations.

**Why it matters:** 
- Inefficient for batch imports
- Real applications need bulk operations
- Reduces API calls

**Where:** Both API applications

**Suggested approach:**

For FastAPI:
```python
class CampaignsBulkCreate(BaseModel):
    campaigns: list[CampaignCreate]

@app.post("/campaigns/bulk", status_code=201)
async def bulk_create_campaigns(data: CampaignsBulkCreate):
    created = []
    for campaign_data in data.campaigns:
        # Create logic here
        created.append(new_campaign)
    return {"created": created, "count": len(created)}
```

**Acceptance criteria:**
- [ ] Add POST /campaigns/bulk endpoint
- [ ] Add PUT /campaigns/bulk endpoint
- [ ] Add DELETE /campaigns/bulk endpoint
- [ ] Validate all items before creating any
- [ ] Return detailed success/failure report
- [ ] Limit batch size (max 100 items)

**Labels:** `feature`, `enhancement`, `priority: low`

---
