
class Hero:
    """     
    Класс дял создания героя 
    
     ...

    Attributes
    ----------
    name : str
        Имя героя
    health : int
        здоровье героя 
    age : int
        age of the person

    Methods
    -------
    print_info():
        Печатает в консоль информацию о герое
    
    kick():
        производит один удар - высчитывает и уменьшает броню и здоровье 
    
    """
    #  свойства класса - каждый созданный объект будет их иметь по умолчанию
    option1 = True
    points = 0
    level = 1

    # конструктор - тут мы создаем свойства которые должны быть у каждого нового объекта
    # и присылаем сюда первоначальные их значения
    def __init__(self, name, health, armor, strong) -> None:
        # свойства объектов
        self.name = name
        self.health = health
        self.armor = armor
        self.strong = strong
    
    # методы - это действия/команды которые могут выполнять объекты
    def _get_info(self):        
        return f"Имя {self.name}\n" \
               f"Здоровье - {self.health}\n" \
               f"Защита {self.armor}"
        
    def print_info(self):
        print(self._get_info() + '\n')
    
    def kick(self, other):        
        other.armor -= self.strong
        if other.armor < 0:
            other.health += other.armor
            other.armor = 0
            

class Mag(Hero):    
    def __init__(self, name, health, armor, strong, mana) -> None:
        # Hero.__init__(self, name, health, armor, strong)
        super().__init__(name, health, armor, strong)
        self.mana = mana
   
    def print_info(self, sep="-"):
        info =  f"{super()._get_info()}\n"  \
                f"{sep*20}\n" \
                f"Мана - {self.mana}\n"
        print(info)


hero1 = Mag('Gendalf', 30, 25, 10, 30,)
hero2 = Mag('Gendalf2', 30, 25, 10, 30,)    
hero2.print_info()
hero1.kick(hero2)
hero2.print_info()

# l = [hero1, hero2]
# print(hero1 in l)
# l.remove(hero1)
# print(l)


# l = [
#     Mag('Gendalf', 30, 25, 10, 30,),
#     Mag('Gendalf2', 30, 25, 10, 30,)   
# ]
