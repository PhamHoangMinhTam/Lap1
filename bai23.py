# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:58:20 2024

@author: TAM PC
"""

import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Phương trình có hai nghiệm phân biệt:", x1,x2 )
elif delta == 0:
    x = -b / (2 * a)
    print("Phương trình có nghiệm kép: ", x1 )
else:
    print("Phương trình vô nghiệm.")