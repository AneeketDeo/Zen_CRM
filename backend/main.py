from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List, Optional
import os
from dotenv import load_dotenv

from database import SessionLocal, engine, Base
from models import User, Contact, Interaction, Task, Deal
from schemas import (
    UserCreate, UserResponse, UserLogin,
    ContactCreate, ContactResponse, ContactUpdate,
    InteractionCreate, InteractionUpdate, InteractionResponse,
    TaskCreate, TaskResponse, TaskUpdate,
    DealCreate, DealResponse, DealUpdate,
    DashboardStats
)
from auth import get_password_hash, verify_password, create_access_token, get_current_user
from crud import (
    create_user, get_user_by_email, get_users,
    create_contact, get_contacts, get_contact, update_contact, delete_contact,
    create_interaction, get_interactions, get_interaction, update_interaction, delete_interaction, get_interactions_by_contact,
    create_task, get_tasks, get_task, update_task, delete_task,
    create_deal, get_deals, get_deal, update_deal, delete_deal,
    get_dashboard_stats
)

load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ZenCRM API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://zen-crm-hazel.vercel.app"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Authentication endpoints
@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    db_user = create_user(db, user, hashed_password)
    return db_user

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db, email=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# User endpoints
@app.get("/users/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/users", response_model=List[UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    users = get_users(db, skip=skip, limit=limit)
    return users

# Contact endpoints
@app.post("/contacts", response_model=ContactResponse)
def create_contact_endpoint(contact: ContactCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_contact(db, contact, current_user.id)

@app.get("/contacts", response_model=List[ContactResponse])
def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    contacts = get_contacts(db, skip=skip, limit=limit, user_id=current_user.id)
    return contacts

@app.get("/contacts/{contact_id}", response_model=ContactResponse)
def read_contact(contact_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    contact = get_contact(db, contact_id=contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@app.put("/contacts/{contact_id}", response_model=ContactResponse)
def update_contact_endpoint(contact_id: int, contact: ContactUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_contact = update_contact(db, contact_id, contact)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@app.delete("/contacts/{contact_id}")
def delete_contact_endpoint(contact_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    success = delete_contact(db, contact_id)
    if not success:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact deleted successfully"}

# Interaction endpoints
@app.post("/interactions", response_model=InteractionResponse)
def create_interaction_endpoint(interaction: InteractionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_interaction(db, interaction, current_user.id)

@app.get("/interactions", response_model=List[InteractionResponse])
def read_interactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    interactions = get_interactions(db, skip=skip, limit=limit, user_id=current_user.id)
    return interactions

@app.get("/interactions/{interaction_id}", response_model=InteractionResponse)
def read_interaction(interaction_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    interaction = get_interaction(db, interaction_id=interaction_id)
    if interaction is None:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return interaction

@app.put("/interactions/{interaction_id}", response_model=InteractionResponse)
def update_interaction_endpoint(interaction_id: int, interaction: InteractionUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_interaction = update_interaction(db, interaction_id, interaction)
    if db_interaction is None:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return db_interaction

@app.delete("/interactions/{interaction_id}")
def delete_interaction_endpoint(interaction_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    success = delete_interaction(db, interaction_id)
    if not success:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return {"message": "Interaction deleted successfully"}

@app.get("/contacts/{contact_id}/interactions", response_model=List[InteractionResponse])
def read_contact_interactions(contact_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    interactions = get_interactions_by_contact(db, contact_id)
    return interactions

# Task endpoints
@app.post("/tasks", response_model=TaskResponse)
def create_task_endpoint(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_task(db, task, current_user.id)

@app.get("/tasks", response_model=List[TaskResponse])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    tasks = get_tasks(db, skip=skip, limit=limit, user_id=current_user.id)
    return tasks

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task_endpoint(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_task = update_task(db, task_id, task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    success = delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}

# Deal endpoints
@app.post("/deals", response_model=DealResponse)
def create_deal_endpoint(deal: DealCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_deal(db, deal, current_user.id)

@app.get("/deals", response_model=List[DealResponse])
def read_deals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    deals = get_deals(db, skip=skip, limit=limit, user_id=current_user.id)
    return deals

@app.get("/deals/{deal_id}", response_model=DealResponse)
def read_deal(deal_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    deal = get_deal(db, deal_id=deal_id)
    if deal is None:
        raise HTTPException(status_code=404, detail="Deal not found")
    return deal

@app.put("/deals/{deal_id}", response_model=DealResponse)
def update_deal_endpoint(deal_id: int, deal: DealUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_deal = update_deal(db, deal_id, deal)
    if db_deal is None:
        raise HTTPException(status_code=404, detail="Deal not found")
    return db_deal

@app.delete("/deals/{deal_id}")
def delete_deal_endpoint(deal_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    success = delete_deal(db, deal_id)
    if not success:
        raise HTTPException(status_code=404, detail="Deal not found")
    return {"message": "Deal deleted successfully"}

# Dashboard endpoints
@app.get("/dashboard/stats", response_model=DashboardStats)
def get_dashboard_stats_endpoint(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_dashboard_stats(db, current_user.id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
