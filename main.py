# -*-coding:UTF8 -*
import os
from thomas import *
from qpe import *

def main():
    #retourne le tableau bien formaté
    dataset, indice = lectureFichier("a_example.txt")

    #Calcul la matrice des tags communs
    m_commonTags = countCommonTags(dataset)
    #Calcul le facteur d'intérêt
    m_interestFactor = interestFactor(dataset, m_commonTags)
    #retourne le ranking  
    slides = outputConstruction(m_interestFactor)
    #slides = [0,2,1]
    
    #écrit les résultats
    ecritureFichier("a_example_result.txt",slides,indice)


main()

