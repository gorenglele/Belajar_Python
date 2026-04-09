import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from module.kalkulator.kalkulator import kurang
from module.kalkulator.kalkulator import *

print(kurang(10, 3))
print(tambah(1, 2))