
# работа с готовыми классами
# from turtle import * 

# t = Turtle(visible=True)
# t1 = Turtle(visible=False)
# t2 = Turtle()

# t1.color('red')
# t2.color('black')



# --------------------------------

#ООП
    # - свойства (атрибуты, поля ) - характеристики
    # - методы (действия)
    


class User:   
    login = ''
    password = '1234'
    
    @staticmethod
    def calc_bd(age):
        return 2005 - age
    
    @classmethod
    def change_pass(cls, new_pass:str):
        cls.password = new_pass
    
    
    def __init__(self, name, age:int, active=True):
        self.name = name
        self.age = age
        self.active = active
        
    def __str__(self):
        return f'{self.name} - {self.age}'
        # return 11
    
    # если нет __str__ принт использует __repr__
    def __repr__(self): # для машин
        return f"User({self.age}, '{self.name}')"
    
    def __len__(self):
        return len(self.name)
    
     # obj1 == obj2
    def __eq__(self, other_obj):
        return self.name == other_obj.name
    
    # obj1 < obj2
    def __lt__(self, other_obj):
        return self.age < other_obj.age
    
    # аналогично
    # __ne__(self, other)   obj1 != obj2
    # __le__(self, other)   obj1 <= obj2
    # __gt__(self, other)   obj1 >  obj2
    # __ge__(self, other)   obj1 >= obj2
    
    def __call__(self, *args, **kwds):
        print(f"Я {self.name}")
        
    def print_info(self):
        print(f" name {self.name} - login - {self.login} / pass - {self.password}")
        


class Users:
    def __init__(self):
        self.users = []
        self.n = 0

    def add(self, user: User):
        self.users.append(user)        
        
    def __len__(self):
        return len(self.users)
    
    def __getitem__(self, val): #obj[0]        
        return self.users[val]
    
    def __setitem__(self, key, value):
        self.users[key] = value
        
    def __iter__(self):        
        return iter(self.users)   
    
         # можно использовать в
        # for i in obj:
        # list(obj)
        # iter(obj)
        # sum(obj)     
        
    def __next__(self):
        if self.n >= len(self.users):
            raise StopIteration
        res =  self.users[self.n]
        self.n+=1
        return res        
        
    

    
user1 = User('User1', 22)
user2 = User('User2', 33)
user3 = User('User3', 44)


print(User)
print(user1)
print(user2)

user1.password = '11111'

print(user2.password)
print(user1.password)

print(user1.__dict__)
print(user2.__dict__)

print(user3.active)
print(user3.age)
user3.age = 55
print(user3.age)

print(user3.password)
print(user1.password)

print(User.password)
User.password = '12345678' # поменяли классовые свойство вручную
print(User.password)
print(user3.password)
User.change_pass('2222222') # поменяли классовые свойство спец методом
print(user3.password)

user1.print_info()
user2.print_info()

print(user1) # __str__ - если __str__ нет ищет __repr__
print(repr(user1)) # __repr__
print(len(user1)) # __len__


print(user1 == user2) # __eq__
print(user1 < user2) # __lt__

l = [user1, user2]
l.sort(reverse=True) # возможно из-за __lt__
print(l)

user1() # __call__

group1 = Users()   

group1.add(user1)
group1.add(user2)
group1.add(user3)

print(len(group1))

print(group1[0]) # __getitem__
group1[0] = user2 # __setitem__
print(group1[0])


for user in group1: #__iter__
    print(user)


# -------------------------------------    
a = 'name123'
# setattr(user1, 'name123', 55) # добавить свойство(атрибут) в любой объект
setattr(user1, a, 55) # добавить свойство(атрибут) в любой объект
getattr(user1, a) # взять значение свойства(атрибута)
# delattr() # удалить атрибут(свойство)
    
    


try:
    print("next", next(group1)) # __next__
    print("next", next(group1)) # __next__
    print("next", next(group1)) # __next__
    print("next", next(group1)) # __next__
except StopIteration:
    print('больше нет')

# -----------------------------------

user4 = User('sasa', 33)
users = [user1, user2, user3]


users2 = [
    User('qqq', 22),
    User('ww', 33),
    User('eee', 44),
    User(name='eee', age=44),
]

for user in users2:
    print(user)
    print(user.name)
    
# -----------------------



# ---------------------------- Менеджер контекста
# class A:
#     def __init__(self):
#         self.con = 1    
    
#     def __enter__(self): # срабатывает при создании объекта с помощью with
#         print(1111)
#         return self.con
        
#     def __exit__(self, q, w, e): # срабатывает когда with закончился
#         self.con=0
#         print(2222)


# # a = A()
# # print(333)
# # a.con=0

# with A() as a:
#     print(a)
#     print(333)        