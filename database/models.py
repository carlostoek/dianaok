from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from database.setup import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    role = Column(String, default='curioso')
    points = Column(Integer, default=0)
    level = Column(Integer, default=1)
    is_vip = Column(Boolean, default=False)

class LorePiece(Base):
    __tablename__ = 'lore_pieces'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    options = Column(String)
    requirements = Column(String)

class UserLorePiece(Base):
    __tablename__ = 'user_lore_pieces'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    lore_id = Column(Integer, ForeignKey('lore_pieces.id'), primary_key=True)
    decision = Column(String)

class Reaction(Base):
    __tablename__ = 'reactions'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    message_id = Column(Integer, primary_key=True)
    emoji = Column(String)

class Badge(Base):
    __tablename__ = 'badges'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    condition = Column(String)

class UserBadge(Base):
    __tablename__ = 'user_badges'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    badge_id = Column(Integer, ForeignKey('badges.id'), primary_key=True)

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    price = Column(Float)
    description = Column(String)

class Inventory(Base):
    __tablename__ = 'inventory'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'), primary_key=True)
    quantity = Column(Integer, default=1)

class Auction(Base):
    __tablename__ = 'auctions'
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('items.id'))
    start_time = Column(DateTime)
    bids = relationship("Bid", back_populates="auction")

class Bid(Base):
    __tablename__ = 'bids'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    auction_id = Column(Integer, ForeignKey('auctions.id'), primary_key=True)
    amount = Column(Float)
    auction = relationship("Auction", back_populates="bids")

class AdminActionLog(Base):
    __tablename__ = 'admin_action_logs'
    id = Column(Integer, primary_key=True, index=True)
    action = Column(String)
    timestamp = Column(DateTime)
    admin_id = Column(Integer, ForeignKey('users.id'))