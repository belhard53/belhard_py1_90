from models.user import User
from services.validation.validator import UserValidator
import random
import string

class PasswordGenerator:
    @staticmethod
    def generate() -> str:
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(10))

class UserFactory:
    @staticmethod
    def create(name: str, login: str, password: str = None) -> User:
        validator = UserValidator()
        validate_field = {"name": name, "login": login}
        if password:
            validate_field |= {'password':password}  
        if not validator.validate(validate_field):
            raise ValueError(f"Invalid user data - {validate_field}")
        
        password = password or PasswordGenerator.generate()
        return User(name, login, password)