from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from .base import Base, IDMixin
from flask_login import UserMixin
from app.extensions import bcrypt


class User(Base, IDMixin, UserMixin):
    __tablename__ = "users"
    
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    
    
    def generate_password_hash(self, pw):
        try:
            hashed = bcrypt.generate_password_hash(pw).decode("utf-8")
            self.password_hash = hashed
            return True
        except Exception, ValueError:
            return False
        
    def check_password_hash(self, pw):
        if not bcrypt.check_password_hash(pw, self.password_hash):
            return {"success": False, "message": "Invalid crednetials povided"}
        else:
            return {"success": True, "user": self}