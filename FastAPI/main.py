"""
FastAPI Campaign Management API

A complete REST API for managing marketing campaigns.
Supports CRUD operations: Create, Read, Update, Delete.

Run with: uvicorn main:app --reload
Docs: http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

app = FastAPI(
    title="Campaign Management API",
    description="Manage marketing campaigns with full CRUD operations",
    version="1.0.0"
)


# Pydantic models for request/response validation
class CampaignCreate(BaseModel):
    """Schema for creating a new campaign"""
    name: str = Field(..., min_length=1, description="Campaign name")
    due_date: datetime = Field(..., description="Campaign due date")


class CampaignUpdate(BaseModel):
    """Schema for updating an existing campaign"""
    name: Optional[str] = Field(None, min_length=1)
    due_date: Optional[datetime] = None


class Campaign(BaseModel):
    """Schema for campaign response"""
    campaign_id: int
    name: str
    due_date: datetime
    created_at: datetime


# In-memory data storage (replace with database in production)
campaigns_db: list[Campaign] = [
    Campaign(
        campaign_id=1,
        name="Summer Launch",
        due_date=datetime(2026, 6, 15),
        created_at=datetime.now()
    ),
    Campaign(
        campaign_id=2,
        name="Black Friday",
        due_date=datetime(2026, 11, 25),
        created_at=datetime.now()
    )
]

# Auto-increment ID counter
next_campaign_id = 3


@app.get('/', tags=["Root"])
async def root():
    """Root endpoint - API information"""
    return {
        "message": "Welcome to Campaign Management API",
        "docs": "/docs",
        "endpoints": {
            "campaigns": "/campaigns"
        }
    }


@app.get("/campaigns", response_model=list[Campaign], tags=["Campaigns"])
async def list_campaigns():
    """Get all campaigns"""
    return campaigns_db


@app.get("/campaigns/{campaign_id}", response_model=Campaign, tags=["Campaigns"])
async def get_campaign(campaign_id: int):
    """Get a specific campaign by ID"""
    for campaign in campaigns_db:
        if campaign.campaign_id == campaign_id:
            return campaign
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Campaign with ID {campaign_id} not found"
    )


@app.post("/campaigns", response_model=Campaign, status_code=status.HTTP_201_CREATED, tags=["Campaigns"])
async def create_campaign(campaign_data: CampaignCreate):
    """Create a new campaign"""
    global next_campaign_id

    new_campaign = Campaign(
        campaign_id=next_campaign_id,
        name=campaign_data.name,
        due_date=campaign_data.due_date,
        created_at=datetime.now()
    )
    campaigns_db.append(new_campaign)
    next_campaign_id += 1

    return new_campaign


@app.put("/campaigns/{campaign_id}", response_model=Campaign, tags=["Campaigns"])
async def update_campaign(campaign_id: int, campaign_update: CampaignUpdate):
    """Update an existing campaign"""
    for campaign in campaigns_db:
        if campaign.campaign_id == campaign_id:
            if campaign_update.name is not None:
                campaign.name = campaign_update.name
            if campaign_update.due_date is not None:
                campaign.due_date = campaign_update.due_date
            return campaign
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Campaign with ID {campaign_id} not found"
    )


@app.delete("/campaigns/{campaign_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Campaigns"])
async def delete_campaign(campaign_id: int):
    """Delete a campaign"""
    for campaign_index, campaign in enumerate(campaigns_db):
        if campaign.campaign_id == campaign_id:
            campaigns_db.pop(campaign_index)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Campaign with ID {campaign_id} not found"
    )
