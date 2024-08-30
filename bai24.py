# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:02:23 2024

@author: TAM PC
"""
gio = int(input("NHap so gio: "))
phut = int(input("Nhap so phut: "))
giay = int(input("Nhap so giay: "))
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print("So gio,phut,giay hop le ")
else:
    print("So gio,phu,giay khong hop le")
