# Управление яркостью монитора по кабелю HDMI используя 
# протокол DDC (Display Data Channel) 

import sys
from monitorcontrol import get_monitors

a = sys.argv

if len(a) == 2 and a[1].isnumeric():
    br = int(a[1])
else:
    br = 10

with get_monitors()[0] as m:
        m.set_luminance(br)
        print(f"Установлена яркость монитора - {br}")