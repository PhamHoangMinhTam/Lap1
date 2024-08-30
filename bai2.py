# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:31:32 2024

@author: Student
"""
a = int(input("Nhập a = "))
b = int(input("Nhập b = "))
tong = a + b
print("Tổng của a và b là =", tong)
hieu = a - b
print("Hiệu của a và b là =", hieu)
tich = a * b
print("Tích của a và b là =", tich)
if b != 0:
    thuong = a / b
    thuong_2_chu_so = round(thuong, 2)
    thuong_3_chu_so = round(thuong, 3)
    print("Thương của a và b là =", thuong_2_chu_so)
    print("Thương của a và b là =", thuong_3_chu_so)
else:
    print("Không thể chia cho 0")
