# -*-coding:UTF8 -*
import os
from thomas import *
from qpe import *

def main():
    #retourne le tableau bien formaté
    dataset, indice = lectureFichier("c_memorable_moments.txt")
    print("lecture OK\n")
    #print(len(indice))
    #Calcul la matrice des tags communs
    """
    m_commonTags = countCommonTags(dataset)
    print("comptage tags en commun OK\n")
    #Calcul le facteur d'intérêt
    m_interestFactor = interestFactor(dataset, m_commonTags)
    print("calcul matrice facteur OK\n")
    """
    m_interestFactor = computeMatrix(dataset)
    print("calcul matrice facteur OK\n")

    #retourne le ranking  
    slides = outputConstruction(m_interestFactor)
    print("calcul suite slides OK\n")
    #print(slides)
    #slides = [0,2,1]
    
    #écrit les résultats
    ecritureFichier("c_memorable_moments_result.txt",slides,indice)
    print("ecriture OK\n")


main()

