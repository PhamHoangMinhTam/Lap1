# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:34:09 2024

@author: Student
"""
from datetime import datetime
nam_sinh= int(input("Nhap nam sinh cua ban"))
nam_hien_tai= datetime.now().year
so_tuoi = nam_hien_tai - nam_sinh
print("Nam sinh cua ban la", so_tuoi)



