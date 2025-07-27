from sqlalchemy.orm import Session
from database import models

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user_id: int, username: str):
    db_user = models.User(id=user_id, username=username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_lore_piece(db: Session, lore_id: int):
    return db.query(models.LorePiece).filter(models.LorePiece.id == lore_id).first()

def add_reaction(db: Session, user_id: int, message_id: int, emoji: str):
    reaction = models.Reaction(user_id=user_id, message_id=message_id, emoji=emoji)
    db.add(reaction)
    db.commit()
    return reaction

# Más funciones de consulta según sea necesario