from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Relationship: One user manages many products
    products = relationship("Product", back_populates="manager")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String) # Product Name (e.g., "Air Max 90")
    stock_count = Column(Integer)  # Renamed from amount
    material_type = Column(String)  # Renamed from category (e.g., "Leather", "Mesh")
    date = Column(DateTime(timezone=True), server_default=func.now())
    
    # Link to the User table
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationship: A product belongs to one manager
    manager = relationship("User", back_populates="products")