import time
# a = time.localtime()
# print(a)
# print(a.tm_year)

from time import time, sleep

# start = time()
# # sleep(1)
# a = 1000**1_000_000
# print(time() - start)


from timeit import timeit

a = list(range(10_000_000))
b = set(a)
c = tuple(a)

print(format(a.__sizeof__(),","))
print(format(b.__sizeof__(),","))
print(format(c.__sizeof__(),","))

print(timeit("111 in a", globals={"a":a}, number=1_000_000))
print(timeit("111 in a", globals={"a":b}))
print(timeit("111 in a", globals={"a":c}))