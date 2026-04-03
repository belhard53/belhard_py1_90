from datetime import datetime, timedelta

from sqlalchemy.orm import Session, joinedload
from database.models import UserDB, ServiceDB, UserServiceDB
from models.interfaces import IUserRepository, IUser
from models.user import User

class UserRepository(IUserRepository):
    def __init__(self, session: Session):
        self._session = session

    def save(self, user: IUser) -> None:
        db_user = UserDB.from_entity(user)
        self._session.add(db_user)
        self._session.commit()

    def get_by_login(self, login: str) -> UserDB | None:
        db_user = self._session.query(UserDB).filter_by(login=login).first()
        return db_user.to_entity() if db_user else None
    
    def get_all(self) -> list[UserDB] | None:
        db_users = self._session.query(UserDB).all()
        users = [db_user.to_entity() for db_user in db_users]
        users = [User.from_db(db_user) for db_user in db_users]
        return users if users else None
    
        
    def add_service_to_user(self, user: IUser, service_id: int) -> bool:
        db_user = self._session.query(UserDB).filter_by(login=user.login).first()
        service = self._session.query(ServiceDB).get(service_id)
        if not service:
            return False
            
        user_service = UserServiceDB(
            user_id=db_user.id,
            service_id=service_id,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=service.period_days)
        )
        self._session.add(user_service)
        self._session.commit()
        return True

    def get_user_with_services(self, user_id: int) -> UserDB | None:
        db_user = self._session.query(UserDB)\
            .options(joinedload(UserDB.services).get(user_id))
        return User.from_db(db_user) if db_user else None