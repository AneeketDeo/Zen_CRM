from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from models import User, Contact, Interaction, Task, Deal, ContactStatus, TaskStatus, DealStage
from schemas import UserCreate, ContactCreate, ContactUpdate, InteractionCreate, TaskCreate, TaskUpdate, DealCreate, DealUpdate, DashboardStats

# User CRUD operations
def create_user(db: Session, user: UserCreate, hashed_password: str):
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

# Contact CRUD operations
def create_contact(db: Session, contact: ContactCreate, owner_id: int):
    db_contact = Contact(**contact.dict(), owner_id=owner_id)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contacts(db: Session, skip: int = 0, limit: int = 100, user_id: Optional[int] = None):
    query = db.query(Contact)
    if user_id:
        query = query.filter(Contact.owner_id == user_id)
    return query.offset(skip).limit(limit).all()

def get_contact(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()

def update_contact(db: Session, contact_id: int, contact: ContactUpdate):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact:
        update_data = contact.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_contact, field, value)
        db.commit()
        db.refresh(db_contact)
    return db_contact

def delete_contact(db: Session, contact_id: int):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact:
        db.delete(db_contact)
        db.commit()
        return True
    return False

# Interaction CRUD operations
def create_interaction(db: Session, interaction: InteractionCreate, user_id: int):
    db_interaction = Interaction(**interaction.dict(), user_id=user_id)
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction

def get_interactions_by_contact(db: Session, contact_id: int):
    return db.query(Interaction).filter(Interaction.contact_id == contact_id).order_by(Interaction.created_at.desc()).all()

# Task CRUD operations
def create_task(db: Session, task: TaskCreate, owner_id: int):
    db_task = Task(**task.dict(), owner_id=owner_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, skip: int = 0, limit: int = 100, user_id: Optional[int] = None):
    query = db.query(Task)
    if user_id:
        query = query.filter(Task.owner_id == user_id)
    return query.offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, task: TaskUpdate):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        update_data = task.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_task, field, value)
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False

# Deal CRUD operations
def create_deal(db: Session, deal: DealCreate, owner_id: int):
    db_deal = Deal(**deal.dict(), owner_id=owner_id)
    db.add(db_deal)
    db.commit()
    db.refresh(db_deal)
    return db_deal

def get_deals(db: Session, skip: int = 0, limit: int = 100, user_id: Optional[int] = None):
    query = db.query(Deal)
    if user_id:
        query = query.filter(Deal.owner_id == user_id)
    return query.offset(skip).limit(limit).all()

def get_deal(db: Session, deal_id: int):
    return db.query(Deal).filter(Deal.id == deal_id).first()

def update_deal(db: Session, deal_id: int, deal: DealUpdate):
    db_deal = db.query(Deal).filter(Deal.id == deal_id).first()
    if db_deal:
        update_data = deal.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_deal, field, value)
        db.commit()
        db.refresh(db_deal)
    return db_deal

def delete_deal(db: Session, deal_id: int):
    db_deal = db.query(Deal).filter(Deal.id == deal_id).first()
    if db_deal:
        db.delete(db_deal)
        db.commit()
        return True
    return False

# Dashboard statistics
def get_dashboard_stats(db: Session, user_id: int):
    # Contact statistics
    total_contacts = db.query(Contact).filter(Contact.owner_id == user_id).count()
    total_leads = db.query(Contact).filter(Contact.owner_id == user_id, Contact.status == ContactStatus.LEAD).count()
    total_prospects = db.query(Contact).filter(Contact.owner_id == user_id, Contact.status == ContactStatus.PROSPECT).count()
    total_customers = db.query(Contact).filter(Contact.owner_id == user_id, Contact.status == ContactStatus.CUSTOMER).count()
    
    # Task statistics
    total_tasks = db.query(Task).filter(Task.owner_id == user_id).count()
    pending_tasks = db.query(Task).filter(Task.owner_id == user_id, Task.status == TaskStatus.PENDING).count()
    completed_tasks = db.query(Task).filter(Task.owner_id == user_id, Task.status == TaskStatus.COMPLETED).count()
    
    # Deal statistics
    total_deals = db.query(Deal).filter(Deal.owner_id == user_id).count()
    total_deal_value = db.query(func.sum(Deal.value)).filter(Deal.owner_id == user_id).scalar() or 0
    
    # Deals by stage
    deals_by_stage = {}
    for stage in DealStage:
        count = db.query(Deal).filter(Deal.owner_id == user_id, Deal.stage == stage).count()
        deals_by_stage[stage.value] = count
    
    # Recent interactions
    recent_interactions = db.query(Interaction).join(Contact).filter(Contact.owner_id == user_id).order_by(Interaction.created_at.desc()).limit(5).all()
    
    return DashboardStats(
        total_contacts=total_contacts,
        total_leads=total_leads,
        total_prospects=total_prospects,
        total_customers=total_customers,
        total_tasks=total_tasks,
        pending_tasks=pending_tasks,
        completed_tasks=completed_tasks,
        total_deals=total_deals,
        total_deal_value=total_deal_value,
        deals_by_stage=deals_by_stage,
        recent_interactions=recent_interactions
    )
