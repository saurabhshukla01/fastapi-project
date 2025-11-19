from app.models.user import User
from app.database.connection import SessionLocal

class UserService:

    def create_user(self, data):
        db = SessionLocal()
        new_user = User(**data.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_users(self):
        db = SessionLocal()
        return db.query(User).all()
