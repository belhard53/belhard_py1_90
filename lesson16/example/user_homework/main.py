from datetime import datetime, timedelta

from database.models import ServiceDB
from database.session import engine, SessionLocal
from factories.user_factory import UserFactory
from repositories.user_repository import UserRepository



def init_db():
    from database.base import Base
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    


def add_test_user(db, repo:UserRepository):
    services = [
        ServiceDB(name="Демо", service_type=0, price=0, period_days=30),
        ServiceDB(name="Премиум", service_type=1, price=299, period_days=365),
        ServiceDB(name="Про", service_type=1, price=599, period_days=30),
    ]
    db.add_all(services)
    
    
    test_users = [
        ("Алексей", "alex123", "Pass123!", False, datetime.now() + timedelta(days=365)),
        ("Мария", "maria88", "Qwerty88", True, datetime.now() - timedelta(days=10)),
        ("Иван", "ivan_1", "Ivan1234", False, datetime.now() + timedelta(days=30)),
        ("Елена", "lenochka", "Leno2023", False, datetime.now() + timedelta(days=180)),
        ("Админ", "admin13", "Adm1245", False, datetime.now() + timedelta(days=999))
    ]
    
    try:
        for name, login, password, is_blocked, sub_date in test_users:
            user = UserFactory.create(
                name=name,
                login=login,
                password=password
            )
            
            user.block(is_blocked)
            user.subscription_date = sub_date            
            repo.save(user)
            repo.add_service_to_user(user, 1)
            print(f"Создан пользователь: {login}")
    
    except Exception as e:
        print(f"Error: {e} ")
    


def main():
    init_db()
    db = SessionLocal()
    user_repo = UserRepository(db)
    add_test_user(db, user_repo)
    
    # try:
    
    user_repo.add_service_to_user(user_repo.get_by_login('alex123'), 2)
    user_repo.add_service_to_user(user_repo.get_by_login('maria88'), 2)
    
    users = user_repo.get_all()
    for user in users:
        print(user)
        for s in user._services:
            print(f'   услуга - {s}')
        # print('---------')
        
    
    
        
    # except Exception as e:
    #     print(f"Error: {e}")
    # finally:
    db.close()

if __name__ == "__main__":
    main()