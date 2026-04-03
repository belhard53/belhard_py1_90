import pytest
from animals import Animal, Cat, Dog, Cow  # подкорректируйте импорт под ваш проект

def test_cat_says():
    cat = Cat(name="Барсик")
    assert cat.says() == "Барсик - кошка. Говорит МЯУ!"

def test_dog_says():
    dog = Dog(name="Рэкс")
    assert dog.says() == "Рэкс - собака. Говорит ГАВ!"

def test_cow_says():
    cow = Cow(name="Мурка")
    assert cow.says() == "Мурка - корова. Говорит МУ-МУ!"

def test_default_name():
    cat = Cat()
    assert cat.name == "SomeName"
    assert cat.says().startswith("SomeName")

def test_animal_abstract_instantiation():
    with pytest.raises(TypeError):
        Animal()
