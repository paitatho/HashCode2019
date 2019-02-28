# -*- coding: utf-8 -*-

import math
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
        for j in range(i, len(dataset)):    
            res = min(m_commonTags[i][j], min(int(dataset[i][0]) - m_commonTags[i][j] , int(dataset[j][0]) - m_commonTags[i][j]))   
            matrice[i][j] = res
            matrice[j][i] = res
    return matrice

m_interestFactor = interestFactor(dt, m_commonTags)
m_interestFactor


def outputConstruction(m_interestFactor):
    # Initialisation
    max_factor = 0
    l,c = 0,0
    rank = []
    for i in range(len(m_interestFactor)):
        for j in range(i,len(m_interestFactor)):
            if max_factor < m_interestFactor[i][j]:
                max_factor = m_interestFactor[i][j]
                l,c = i,j
    rank.append(l)
    rank.append(c)
    print(rank)
    print(rank[-1])
    max_factor = 0
    while len(rank) != len(m_interestFactor):
        c = rank[-1]
        for i in range(len(m_interestFactor)):
            if i not in rank and max_factor < m_interestFactor[i][c]:
                max_factor = 0
                l = i
        rank.append(l)                    
    return rank

m_interestFactor
rank = outputConstruction(m_interestFactor)
    

 