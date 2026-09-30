from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./fitbuddy.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True)
    username = Column(String)
    age = Column(Integer)
    weight = Column(String)
    goal = Column(String)
    intensity = Column(String)

class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    original_plan = Column(Text)
    updated_plan = Column(Text, nullable=True)
    nutrition_tip = Column(Text)

Base.metadata.create_all(bind=engine)

def save_user(data):
    db = SessionLocal()
    try:
        user = User(**data)
        db.add(user)
        db.commit()
    finally:
        db.close()

def save_plan(data):
    db = SessionLocal()
    try:
        plan = Plan(**data)
        db.add(plan)
        db.commit()
    finally:
        db.close()

def get_plan(user_id):
    db = SessionLocal()
    try:
        return db.query(Plan).filter(Plan.user_id == user_id).first()
    finally:
        db.close()

def update_plan(user_id, updated_plan):
    db = SessionLocal()
    try:
        plan = get_plan(user_id)
        if plan:
            plan.updated_plan = updated_plan
            db.commit()
    finally:
        db.close()

def get_all_users():
    db = SessionLocal()
    try:
        return db.query(User).all()
    finally:
        db.close()

def get_all_plans():
    db = SessionLocal()
    try:
        return db.query(Plan).all()
    finally:
        db.close()
