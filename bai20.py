# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:22:40 2024

@author: TAM PC
"""
a = int(input("Nhap so nguyen a "))
b = int(input("Nhap so nguyen b "))
c = int(input("Nhap so nguyen c "))
so_lon_nhat = a
if b > so_lon_nhat:
    so_lon_nhat = b
if c > so_lon_nhat:
    so_lon_nhat = c
print("So nguyen lon nhat la", so_lon_nhat)

