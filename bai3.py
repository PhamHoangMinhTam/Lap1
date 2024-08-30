# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:31:44 2024

@author: Student
"""

a= int(input("Nhap a ="))
b= int(input("Nhap b ="))
if b!= 0:
  chia_lay_nguyen = a // b
  print("Chia lay nguyen = ",a//b)
  chia_lay_du = a % b
  print("Chia lay du = ", a % b)
  chia_thuc = a/b
  print("Chia thuc = ", a/ b)
else:
    print("Khong the chia cho 0")