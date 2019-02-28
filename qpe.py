# -*- coding: utf-8 -*-

import math
import numpy as np
import itertools as it
from thomas import *


dataset = lectureFichier('a_example.txt')
dataset.pop(0)
dataset = dataset[:-1]
dataset

dt = [x[1:] for x in dataset]
dt

def countCommonTags(dataset):
    matrice = [[0]*len(dataset) for _ in range(len(dataset))]
    for i,x in enumerate(dataset):
        for j,y in enumerate(dataset):
            matrice[i][j] = len(x[1:]) + len(y[1:]) - len(set(x[1:] + y[1:])) 
    return matrice

m_commonTags = countCommonTags(dt)
m_commonTags

def interestFactor(dataset, m_commonTags):
    matrice = [[0]*len(dataset) for _ in range(len(dataset))]
    for i in range(len(dataset)):
        for j in range(len(dataset)):    
            res = min(m_commonTags[i][j], min(int(dataset[i][0]) - m_commonTags[i][j] , int(dataset[j][0]) - m_commonTags[i][j]))   
            matrice[i][j] = res
    print(matrice)
    return matrice

m_interestFactor = interestFactor(dt, m_commonTags)
print(m_interestFactor)

    