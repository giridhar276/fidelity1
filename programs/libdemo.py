
# method1 - all the methods are imported to your program
import math 
print(math.floor(34.4))
print(math.log(2))

# method2 - importing with alias name
import math as m 
print(m.tan(1))
print(m.cos(1))

# method3 - importing required methods ONLY 
from math import tan,cos 
print(tan(1))
print(cos(2))

from math import tan as t,cos as c
print(t(1))
print(c(2))



import shutil 
import os 
import psutil 
import datetime 
print(datetime.datetime.now())
import time 
print(time.ctime())
import calendar
print(calendar.calendar(2025))
print(calendar.month(2025,11))
import platform
print(platform.node())
import random 
print(random.random())
print(random.randrange(1000,9999))
import requests 
response = requests.get("https://www.google.com/")
print(response.text)

