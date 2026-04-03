from .strategies import (
    RussianNameValidator,
    LoginValidator,
    PasswordValidator
)

class UserValidator:
    def __init__(self):
        self._validators = {
            "name": RussianNameValidator(),
            "login": LoginValidator(),
            "password": PasswordValidator(),
            
        }

    def validate(self, user_data: dict) -> bool:
        return all(
            self._validators[key].validate(user_data[key])
            for key in user_data
        )