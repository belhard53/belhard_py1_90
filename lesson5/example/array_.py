# классические массивы в python

# 'b'  → signed char     (1)
# 'B'  → unsigned char   (1)  
# 'h'  → signed short    (2)
# 'H'  → unsigned short  (2)
# 'i'  → signed int      (4)
# 'I'  → unsigned int    (4)
# 'f'  → float           (4)
# 'd'  → double          (8)

import array

# 'i' = signed int (4 байта)
a = array.array('i', [85, 92, 78, 95, 88])
print(a)           
print(a[0])        
a.append(100)
print(a[-1])       

# объект array в памяти занимает меньше места

# numpy

