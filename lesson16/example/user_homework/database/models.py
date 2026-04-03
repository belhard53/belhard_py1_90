from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base
from models.user import User

class UserDB(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    login = Column(String(30), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_blocked = Column(Boolean, default=False)
    subscription_date = Column(DateTime)

    @classmethod
    def from_entity(cls, user: User) -> "UserDB":
        return cls(
            name=user.name,
            login=user.login,
            password=user.password,
            is_blocked=user.is_blocked,
            subscription_date=user.subscription_date
        )

    def to_entity(self) -> User:
        return User(
            name=self.name,
            login=self.login,
            password=self.password
        )
        
        
class ServiceDB(Base):
    __tablename__ = 'services'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    service_type = Column(Integer)  # 1 - платная, 0 - бесплатная
    price = Column(Float)
    period_days = Column(Integer)        
    
    
class UserServiceDB(Base):
    __tablename__ = 'user_services'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    
    service = relationship("ServiceDB", backref="users")
    user = relationship("UserDB", backref="services")    