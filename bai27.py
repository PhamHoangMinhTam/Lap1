# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:51:12 2024

@author: TAM PC
"""
import math 
hinh = input("Nhập loại hình (v - hình vuông, n - hình chữ nhật, t - hình tròn): ").lower()

if hinh == 'v':
    canh = float(input("Nhập chiều dài cạnh hình vuông: "))
    chu_vi = 4 * canh
    dien_tich = canh * canh
    print("Chu vi của hình vuông là:", chu_vi)
    print("Diện tích của hình vuông là:", dien_tich)

elif hinh == 'n':
    rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    dai = float(input("Nhập chiều dài hình chữ nhật: "))
    chu_vi = 2 * (rong + dai)
    dien_tich = rong * dai
    print("Chu vi của hình chữ nhật là:", chu_vi)
    print("Diện tích của hình chữ nhật là:", dien_tich)

elif hinh == 't':
    ban_kinh = float(input("Nhập bán kính hình tròn: "))
    chu_vi = 2 * math.pi * ban_kinh
    dien_tich = math.pi * (ban_kinh ** 2)
    print("Chu vi của hình tròn là:", chu_vi)
    print("Diện tích của hình tròn là:", dien_tich)
