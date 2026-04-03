import pytest
from user import User 

def test_create_user():
    user = User("Ivan", "Petrov", 28)
    assert user.fname == "Ivan"
    assert user.lname == "Petrov"
    assert user.age == 28

def test_full_name():
    user = User("Anna", "Sidorova", 34)
    assert user.full_name() == "Anna Sidorova"

def test_is_adult_true():
    user = User("Pavel", "Ivanov", 22)
    assert user.is_adult() is True

def test_is_adult_false():
    user = User("Olga", "Smirnova", 17)
    assert not user.is_adult()

@pytest.mark.parametrize("fname, lname, age, expected", [
    ("Dmitry", "Kuznetsov", 31, True),
    ("Elena", "Novikova", 15, False),
    ("Sergey", "Fedorov", 40, True),
])
def test_param_is_adult(fname, lname, age, expected):
    user = User(fname, lname, age)
    assert user.is_adult() == expected


if __name__ == "__main__":
    pytest.main([__file__])

    import sys
    # sys.exit(pytest.main([__file__]))
    
    
    



# запускать так
# pytest lesson16\example\testing\test_user.py