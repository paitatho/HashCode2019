# -*-coding:UTF8 -*
import os
from thomas import *
#from qpe import *

def main():
    #retourne le tableau bien formaté
    resultat, indice = lectureFichier("a_example.txt")

    #ajouter fonction quentin 
    slides =[0,2,1]

    #écrit les résultats
    ecritureFichier("a_example_result.txt",slides,indice)



main()

