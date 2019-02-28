# -*- coding: utf-8 -*-

def computeMatrix(dataset):
    n = len(dataset)
    matrice = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            x = dataset[i]
            y = dataset[j]
            res = len(x[1:]) + len(y[1:]) - len(set(x[1:] + y[1:]))
            matrice[i][j] = min(res, min(int(dataset[i][0]) - res , int(dataset[j][0]) - res))
            matrice[j][i] = matrice[i][j]
    return matrice

"""
def countCommonTags(dataset):
    matrice = [[0]*len(dataset) for _ in range(len(dataset))]
    for i,x in enumerate(dataset):
        for j,y in enumerate(dataset):
            matrice[i][j] = len(x[1:]) + len(y[1:]) - len(set(x[1:] + y[1:])) 
    return matrice

def interestFactor(dataset, m_commonTags):
    matrice = [[0]*len(dataset) for _ in range(len(dataset))]
    for i in range(len(dataset)):
        for j in range(i, len(dataset)):    
            res = min(m_commonTags[i][j], min(int(dataset[i][0]) - m_commonTags[i][j] , int(dataset[j][0]) - m_commonTags[i][j]))   
            matrice[i][j] = res
            matrice[j][i] = res
    return matrice


def computeMatrix(dataset):
    m_commonTags = countCommonTags(dataset)
    m_interestFactor = interestFactor(dataset, m_commonTags)
    return m_interestFactor
"""


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
    not_attributed = list(range(len(m_interestFactor)))
    rank.append(l)
    not_attributed.remove(l)
    rank.append(c)
    not_attributed.remove(c)    
    while len(rank) != len(m_interestFactor):
        c = rank[-1]
        max_factor = 0
        for i in not_attributed:
             if max_factor <= m_interestFactor[c][i]:
                max_factor = m_interestFactor[c][i]
                l = i
        rank.append(l)                    
        not_attributed.remove(l)
    return rank
    

 
