# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:58:03 2024

@author: TAM PC
"""
a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
import math
A = ((a + b)/(math.pow(a,1/3))) - (math.pow(a*b,1/3))
B = (math.pow(a,1/3)) - math.pow(b,1/3)
print("Giá trị biểu thức:",round(A/B,2))


