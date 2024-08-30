# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:32:20 2024

@author: Student
"""

N = int(input("Nhap so nguyen duong N ="))
if 10 <= N <= 99:
    chuc = N // 10
    don_vi = N % 10
    tong = chuc + don_vi
    print("Tong chu so nguyen duong cua N la", tong)
else:
    print("Khong phai so nguyen duong co hai chu so")