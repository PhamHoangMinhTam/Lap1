# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:12:51 2024

@author: TAM PC
"""
a = int(input("Nhap so nguyen a "))
b = int(input("Nhap so nguyen b "))
c = int(input("Nhap so nguyen c "))
d = int(input("Nhap so nguyen d "))
so_nho_nhat = a
if b < so_nho_nhat:
    so_nho_nhat = b
if c < so_nho_nhat:
    so_nho_nhat = c
if d < so_nho_nhat :
    so_nho_nhat = d
print("So nguyen nho nhat la ", so_nho_nhat)
