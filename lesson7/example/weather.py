# pip install pyowm

# если venv
# pip install --upgrade setuptools


from pyowm import OWM
from pprint import pprint

owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d')
mgr = owm.weather_manager()


# print(dir(str))
# print(dir(mgr))

w = mgr.weather_at_place('Minsk')
# print(dir(w))
ww = w.to_dict()


pprint(ww)
