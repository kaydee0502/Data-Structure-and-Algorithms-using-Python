# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:38:51 2020

@author: KayDee
"""

from collections import namedtuple

car = namedtuple("Cars", ['Normal','jdm','exotic'])


favcar = car(Normal = 'Kwid',jdm = 'evo', exotic = 'porche')
print(favcar.jdm)

okcar = car(Normal = 'Swift',jdm = 'BRZ' ,exotic = 'lambo')