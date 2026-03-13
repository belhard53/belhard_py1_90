# f = open('test1.txt', 'w')
# f.close()

import os

BASE_DIR = os.path.dirname(__file__)
file_name = os.path.join(BASE_DIR, "test1.txt")

with open(file_name, 'w', encoding='utf-8') as f:
    f.write("Hello python1\n")
    f.write("Привет python2\n")
    
with open(file_name, 'a', encoding='utf-8') as f:
    f.write("Hello python1\n")
    f.write("Привет python2\n")
    
with open(file_name, 'r', encoding='utf-8') as f:    
    # a = f.read()
    # a = f.readline()
    # a = f.readlines()
    # print(a)
    
    for line in f:
        print(line)
    
print('ok')    



