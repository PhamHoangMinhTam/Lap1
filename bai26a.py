# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:40:39 2024

@author: TAM PC
"""
a = float(input("Nhap a: ")) 
b = float(input("Nhap b: ")) 
c = float(input("Nhap c: ")) 
if a > b:
    a,b = b,a 
if b > c:
    b,c = c,b
if a > c:
    a,c = c,a
print("Theo thu tu tang dan la", a ,b ,c)
