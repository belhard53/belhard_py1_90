"""
Комплексные тесты для класса User
Проверяет: валидацию, генерацию пароля, подписку, блокировку
"""

import pytest
from datetime import date, timedelta
from your_module import User  # Заменить на импорт вашего класса


class TestUser:
    
    def test_create_valid_user(self):
        """Создание с валидными данными"""
        user = User("Иван", "ivan123", "Abc1D2")
        assert user.name == "Иван"
        assert user.login == "ivan123"
        assert len(user.password) >= 6
        assert user.is_blocked is False
        assert user.subscription_mode == "free"
        assert user.subscription_date > date.today()
    
    def test_generate_password(self):
        """Автогенерация пароля"""
        user = User("Петя", "petya456")
        assert len(user.password) >= 6
        assert any(c.islower() for c in user.password)
        assert any(c.isupper() for c in user.password)
        assert any(c.isdigit() for c in user.password)
    
    def test_invalid_name_raises(self):
        """Невалидное имя → ValueError"""
        with pytest.raises(ValueError, match="русского алфавита"):
            User("Ivan", "ivan123")
    
    def test_invalid_login_raises(self):
        """Невалидный логин → ValueError"""
        with pytest.raises(ValueError, match="не менее 6 символов"):
            User("Иван", "iv")
    
    def test_invalid_password_raises(self):
        """Невалидный пароль → ValueError"""
        with pytest.raises(ValueError, match="более шести символов"):
            User("Иван", "ivan123", "abc")
    
    def test_block_unblock(self):
        """Блокировка/разблокировка"""
        user = User("Катя", "katya_katya")
        assert not user.is_blocked
        
        user.bloc(True)
        assert user.is_blocked
        
        user.bloc(False)
        assert not user.is_blocked
    
    def test_subscription_check_active(self):
        """Активная подписка"""
        user = User("Оля", "olya_abc")
        active, mode, days = user.check_subscr()
        assert active is True
        assert mode == "free"
        assert days >= 0
    
    def test_subscription_expired(self):
        """Истекшая подписка"""
        user = User("Маша", "masha_789", subscription_date=date.today())
        active, _, days = user.check_subscr()
        assert active is False
        assert days == 0  # max(0, negative)
    
    def test_extend_subscription(self):
        """Продление подписки"""
        user = User("Вася", "vasya_123")
        old_date = user.subscription_date
        user.extend_subscription(15)
        assert user.subscription_date == old_date + timedelta(days=15)
        assert user.subscription_mode == "paid"
    
    def test_change_password(self):
        """Смена пароля"""
        user = User("Петя", "petya456")
        old_pass = user.password
        
        # Генерация нового
        new_pass = user.change_pass()
        assert new_pass != old_pass
        assert len(new_pass) >= 6
        
        # Установка своего
        user.change_pass("NewPass123")
        assert user.password == "NewPass123"
    
    def test_get_info_blocked(self):
        """Инфо о заблокированном"""
        user = User("Иван", "ivan_ivan")
        user.bloc(True)
        assert "заблокирован" in user.get_info()
    
    def test_get_info_normal(self):
        """Обычная информация"""
        user = User("Катя", "katya_katya")
        info = user.get_info()
        assert "Катя" in info
        assert "katya_katya" in info
        assert user.subscription_mode in info
    
    def test_subscription_date_future(self):
        """Подписка на будущую дату"""
        user = User("Оля", "olya_abc")
        future_date = date.today() + timedelta(days=10)
        active, _, _ = user.check_subscr(future_date)
        assert active is False  # Подписка ещё не началась


def test_manual_demo():
    """Демо для ручной проверки"""
    print("=== ДЕМО КЛАССА USER ===\n")
    
    # 1. Создание с автопаролем
    print("1. Создание с автопаролем:")
    u1 = User("Вася", "vasya123")
    print(u1.get_info())
    
    # 2. Продление
    print("\n2. Продление подписки:")
    u1.extend_subscription(60)
    print(u1.get_info())
    
    # 3. Смена пароля
    print("\n3. Смена пароля:")
    new_pass = u1.change_pass("SuperSecure2025!")
    print(f"Новый пароль: {new_pass}")
    
    # 4. Блокировка
    print("\n4. Блокировка:")
    u1.bloc(True)
    print(u1.get_info())
    
    # 5. Проверка подписки
    print("\n5. Статус подписки:")
    active, mode, days = u1.check_subscr()
    print(f"Активна: {active}, Режим: {mode}, Дней: {days}")


if __name__ == "__main__":
    # Запуск pytest
    pytest.main(["-v", __file__])
    
    print("\n" + "="*50)
    # Демо
    test_manual_demo()



# # Установка pytest
# pip install pytest

# # Запуск
# python test_user.py
# # или
# pytest test_user.py -v