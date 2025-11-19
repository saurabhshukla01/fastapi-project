from app.models.user import User
from app.database.connection import SessionLocal

def seed():
    db = SessionLocal()
    user = User(username="admin", email="admin@example.com")
    db.add(user)
    db.commit()
