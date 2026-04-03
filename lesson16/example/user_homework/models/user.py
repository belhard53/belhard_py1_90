from datetime import datetime, timedelta

# from database.models import UserDB
from .interfaces import IUser

class User(IUser):
    def __init__(self, name: str, login: str, password: str, id=None):
        self.id = id
        self.__name = name
        self.login = login
        self.password = password
        self.is_blocked = False        
        self._services: list[UserService] = []

    def __str__(self):
        # return f"{self.name} {self.login} / {self._services}"
        return f"{self.name} {self.login}"

    @property
    def name(self) -> str: return self.__name
    
    def block(self, status: bool) -> None:
        self._is_blocked = status

    def check_subscription(self, date: datetime = None) -> dict:
        check_date = date or datetime.now()
        return {
            "is_active": check_date <= self.subscription_date,
            "mode": self.subscription_mode
        }
    
    def add_service(self, service_id: int, name: str, period_days: int) -> None:
        now = datetime.now()
        end_date = now + timedelta(days=period_days)
        self._services.append(
            UserService(service_id, name, now, end_date)
        )

    def extend_service(self, service_id: int, period_days: int) -> bool:
        for service in self._services:
            if service.service_id == service_id and service.is_active:
                service.end_date += timedelta(days=period_days)
                return True
        return False

    def remove_service(self, service_id: int) -> bool:
        for i, service in enumerate(self._services):
            if service.service_id == service_id:
                self._services.pop(i)
                return True
        return False
    
    
    def get_active_services(self) -> list[dict]:
        return [
            {
                "id": s.service_id,
                "name": s.name,
                "start_date": s.start_date,
                "end_date": s.end_date,
                "is_active": s.is_active
            }
            for s in self._services
        ]
    
    @classmethod
    def from_db(cls, db_user):
        user = cls(
            id=db_user.id,
            name=db_user.name,
            login=db_user.login,
            password=db_user.password
        )
        user._is_blocked = db_user.is_blocked
        
        for user_service in db_user.services:
            user.add_service(
                service_id=user_service.service_id,
                name=user_service.service.name,
                period_days=(user_service.end_date - user_service.start_date).days
            )
        return user
    
    
        
class UserService:
    def __init__(self, service_id: int, name: str, start_date: datetime, end_date: datetime):
        self.service_id = service_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
    
    def __str__(self):
        return f"{self.name} до {self.end_date:%d.%m.%Y}"

    @property
    def is_active(self) -> bool:
        return datetime.now() < self.end_date        