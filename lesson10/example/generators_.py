a = [i**10 for i in range(1_000_000)]
b = (i**10 for i in range(1_000_000))

print(a.__sizeof__())
print(b.__sizeof__())

import timeit
print('---')
print(timeit.timeit('for _ in a:pass', number=100, globals={'a':a})) 
print(timeit.timeit('for _ in b:pass', number=100, globals={'b':b})) 

print('---')
b = (i**10 for i in range(1_000_000))
print(timeit.timeit('sum(a)', number=100, globals={'a':a})) 
print(timeit.timeit('sum(b)', number=100, globals={'b':b})) 

print('---')
b = (i**10 for i in range(1_000_000))
print(timeit.timeit('any(a)', number=100000, globals={'a':a})) 
print(timeit.timeit('any(b)', number=100000, globals={'b':b})) 

print('---')
print(timeit.timeit('sum([x for x in range(1_000_000)])', number=100)) 
print(timeit.timeit('sum(x for x in range(1_000_000))', number=100)) 

# -------------

# a = [i**2 for i in range(10)]
# b = (i**2 for i in range(10))
# print(type(a), type(b))

# for i in a:
#     print(i)
# print('-----------')    
# for i in b:
#     print(i)
    
# print('-----------')    
# for i in b:
#     print(i)    
    
# -----------------------------    

# def f1():
#     print(11)
#     yield 1
#     print(22)
#     yield 2
    
# a = f1()    
# print(a)
# print(next(a))
# print(next(a))
# # print(next(a))
# print('-----')

# for i in f1():
#     print(i)
    
# for i in f1():
#     print(i)    
    
# --------------------------
    
# def f1(n):
#     for i in range(1, n):
#         yield i**2 + i
        
# for i in f1(100):
#     print(i) 

# import time
    
# def f2(n):
#     while 1:
#         yield time.time()


# ---------------------------

# --------------
# def f1():
#     yield 111
#     yield 222
#     yield 333
    
# def f2():
#     yield 11111
#     yield 22222
#     yield 33333
    
# def f3(a=f1(), b=f2()):        
#     while 1:
#         try:
#             yield next(a)
#             yield next(b)
#         except StopIteration:
#             break

# for item in f3():
#     print(item)

# -----------------------------


# def ping():
#     yield "ping1"
#     yield "ping2"
#     yield "ping3"

# def main():
#     yield "start"
#     yield from ping()
#     yield "end"

# # for x in main():
# #     print(x)
    
#     # ------------------
    
# def f1():
#     yield from "QWER"
#     yield from range(1, 5)
#     yield from ping()
    
# for i in f1():
#     print(i)

    