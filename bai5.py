# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:32:34 2024

@author: Student
"""

time = input("Nhập vào giờ, phút và giây theo định dạng hh:mm:ss = ")
hh, mm , ss = map(int, time.split(":"))
tong_so_giay = hh * 3600 + mm * 60 + ss
print("Tong so giay la", tong_so_giay)