import re
from abc import ABC, abstractmethod

class ValidationStrategy(ABC):
    @abstractmethod
    def validate(self, value: str) -> bool: ...

class RussianNameValidator(ValidationStrategy):
    def validate(self, value: str) -> bool:
        return bool(re.fullmatch(r'^[а-яА-ЯёЁ]+$', value))

class LoginValidator(ValidationStrategy):
    def validate(self, value: str) -> bool:
        return bool(re.fullmatch(r'^[a-zA-Z0-9_]{6,}$', value))

class PasswordValidator(ValidationStrategy):
    def validate(self, value: str) -> bool:
        return (len(value) >= 6 and 
                any(c.isupper() for c in value) and
                any(c.isdigit() for c in value))