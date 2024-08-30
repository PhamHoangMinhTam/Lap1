# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:13:23 2024

@author: TAM PC
"""
chu_cai = input("Nhập một chữ cái: ")
if chu_cai.islower():
    ket_qua = chu_cai.upper()
else:
    ket_qua = chu_cai.lower()
print("Ki tu sau khi chuyen doi la", ket_qua)
