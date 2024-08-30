# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:46:00 2024

@author: TAM PC
"""
N = input("Nhập một số nguyên: ")
danh_sach_chu_so = list(N)
danh_sach_chu_so.sort()
so_sap_xep = ''.join(danh_sach_chu_so)
print("Số có các chữ số theo thứ tự tăng dần là:", so_sap_xep)

