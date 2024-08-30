# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:32:33 2024

@author: TAM PC
"""
def tinh_so_nut(so_xe):
    while so_xe >= 10:
        so_xe = sum(int(chu_so) for chu_so in str(so_xe))
    return so_xe
so_xe = int(input("Nhập số xe: "))
so_nut = tinh_so_nut(so_xe)
print(f"Số nút của số xe là: {so_nut}")
