from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, Dict

class IUser(ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def block(self, status: bool) -> None: ...

    @abstractmethod
    def check_subscription(self, date: Optional[datetime] = None) -> Dict: ...

class IUserRepository(ABC):
    @abstractmethod
    def save(self, user: IUser) -> None: ...

    @abstractmethod
    def get_by_login(self, login: str) -> Optional[IUser]: ...