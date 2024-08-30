# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:52:37 2024

@author: TAM PC
"""
so_thu_nhat = int(input("Nhap so nguyen thu nhat "))
so_thu_hai = int(input("Nhap so nguyen thu hai "))
so_thu_ba = int(input("Nhap so nguyen thu ba "))
so_lon_nhat = max(so_thu_nhat,so_thu_hai,so_thu_ba)
so_nho_nhat = min(so_thu_nhat,so_thu_hai,so_thu_ba)
print("So nguyen lon nhat la ", so_lon_nhat)
print("so nguyen nho nhat la ", so_nho_nhat)

