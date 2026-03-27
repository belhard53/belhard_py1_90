'''
random()	Вещественное [0.0, 1.0)	random.random() → 0.734
randint(a, b)	Целое [a, b] включительно	random.randint(1, 10) → 7
randrange(stop)	Целое [0, stop)	random.randrange(10) → 3
randrange(start, stop, step)	С шагом	random.randrange(0, 20, 2) → 4
uniform(a, b)	Вещественное [a, b]	random.uniform(1.5, 5.5) → 3.21
choice(seq)	Случайный элемент	random.choice(['a','b','c']) → 'b'
choices(seq, k=n)	k элементов с повтором	random.choices([1,2,3], k=3)
sample(seq, k)	k уникальных элементов	random.sample([1,2,3,4], 2) → [3,1]
shuffle(seq)	Перемешать список на месте	random.shuffle(my_list)
seed(n)	Инициализация для воспроизводимости	random.seed(4

'''


import random as r
# r.seed(1)
a = [r.randint(1, 10) for _ in range(10)]
print(a)

