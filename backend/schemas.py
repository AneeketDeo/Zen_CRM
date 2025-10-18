from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List
from datetime import datetime
from models import UserRole, ContactStatus, InteractionType, TaskPriority, TaskStatus, DealStage

# User schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: UserRole = UserRole.USER

class UserCreate(UserBase):
    password: str
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        # No maximum length limit with Argon2 - much more secure than bcrypt
        return v

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Contact schemas
class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    position: Optional[str] = None
    status: ContactStatus = ContactStatus.LEAD
    notes: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class ContactUpdate(ContactBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class ContactResponse(ContactBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Interaction schemas
class InteractionBase(BaseModel):
    type: InteractionType
    subject: str
    notes: Optional[str] = None
    scheduled_date: Optional[datetime] = None

class InteractionCreate(InteractionBase):
    contact_id: int

class InteractionUpdate(InteractionBase):
    contact_id: Optional[int] = None

class InteractionResponse(InteractionBase):
    id: int
    contact_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Task schemas
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: TaskPriority = TaskPriority.MEDIUM
    status: TaskStatus = TaskStatus.PENDING
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    contact_id: Optional[int] = None

class TaskUpdate(TaskBase):
    title: Optional[str] = None

class TaskResponse(TaskBase):
    id: int
    contact_id: Optional[int]
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Deal schemas
class DealBase(BaseModel):
    title: str
    description: Optional[str] = None
    value: Optional[float] = None
    stage: DealStage = DealStage.PROSPECTING
    probability: int = 0
    expected_close_date: Optional[datetime] = None

class DealCreate(DealBase):
    contact_id: int

class DealUpdate(DealBase):
    title: Optional[str] = None

class DealResponse(DealBase):
    id: int
    contact_id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Dashboard schemas
class DashboardStats(BaseModel):
    total_contacts: int
    total_leads: int
    total_prospects: int
    total_customers: int
    total_tasks: int
    pending_tasks: int
    completed_tasks: int
    total_deals: int
    total_deal_value: float
    deals_by_stage: dict
    recent_interactions: List[InteractionResponse]
