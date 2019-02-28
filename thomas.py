# -*-coding:UTF8 -*
from math import *

def lectureFichier():
    mon_fichier = open("a_example.txt", "r")
    contenu = mon_fichier.read()
    contenu = contenu.split("\n")

    for i in range(0,len(contenu)):
        contenu[i] = contenu[i].split(" ")
        
    return contenu

lectureFichier()
