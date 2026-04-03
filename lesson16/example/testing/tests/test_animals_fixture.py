import pytest
from animals import Animal, Cat, Dog, Cow

@pytest.fixture
def cat():
    return Cat(name="Барсик")

@pytest.fixture
def dog():
    return Dog(name="Рэкс")

@pytest.fixture
def cow():
    return Cow(name="Мурка")

def test_cat_says(cat):
    assert cat.says() == "Барсик - кошка. Говорит МЯУ!"

def test_dog_says(dog):
    assert dog.says() == "Рэкс - собака. Говорит ГАВ!"

def test_cow_says(cow):
    assert cow.says() == "Мурка - корова. Говорит МУ-МУ!"

def test_default_name():
    cat = Cat()
    assert cat.name == "SomeName"
    assert cat.says().startswith("SomeName")

def test_animal_abstract_instantiation():
    with pytest.raises(TypeError):
        Animal()
