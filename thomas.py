# -*-coding:UTF8 -*
from math import *

def lectureFichier(filepath):
    mon_fichier = open(filepath, "r")
    contenu = mon_fichier.read()
    contenu = contenu.split("\n")

    for i in range(0,len(contenu)):
        contenu[i] = contenu[i].split(" ")
        
    return contenu

