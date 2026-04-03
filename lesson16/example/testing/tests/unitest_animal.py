import unittest

from animals import *

class TestAnimals(unittest.TestCase):

    def test_cat_says(self):
        cat = Cat(name="Барсик")
        expected = "Барсик - кошка. Говорит МЯУ!"
        self.assertEqual(cat.says(), expected)

    def test_dog_says(self):
        dog = Dog(name="Рэкс")
        expected = "Рэкс - собака. Говорит ГАВ!"
        self.assertEqual(dog.says(), expected)

    def test_cow_says(self):
        cow = Cow(name="Мурка")
        expected = "Мурка - корова. Говорит МУ-МУ!"
        self.assertEqual(cow.says(), expected)

    def test_default_name(self):
        # Проверяем, что имя по умолчанию "SomeName"
        cat = Cat()
        self.assertTrue(cat.name == "SomeName")
        self.assertTrue(cat.says().startswith("SomeName"))

    def test_animal_abstract(self):
        # Проверяем, что нельзя создать экземпляр Animal напрямую
        with self.assertRaises(TypeError):
            animal = Animal()

if __name__ == "__main__":
    unittest.main()