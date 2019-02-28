# -*-coding:UTF8 -*
from math import *

def lectureFichier(filepath):
    mon_fichier = open(filepath, "r")
    contenu = mon_fichier.read()
    contenu = contenu.split("\n")
    contenu.pop(0)
    contenu.pop(len(contenu)-1)
    for i in range(0,len(contenu)):
        contenu[i] = contenu[i].split(" ")
        contenu[i].insert(0,i)

    resultat, indice = mergeVertical(contenu)
    #print(resultat);print(indice)
    return resultat, indice


def mergeVertical(liste):
    indice1 = -1
    result = list()
    tabIndice = list()
    for i in range(0,len(liste)):
        if liste[i][1] == 'V':
            if indice1 == -1:
                indice1 = i
                tmp = liste[i][3:]
            else :
                tmp = tmp + liste[i][3:]
                merge = list(set(tmp))
                merge.insert(0,len(merge))
                result.append(merge)
                tabIndice.append([indice1,i])
                tmp =[]
                indice1 = -1
                
        else:
            result.append(liste[i][2:])
            tabIndice.append([liste[i][0]])
    return result, tabIndice

def ecritureFichier(filePath, slides, indice):
    mon_fichier = open(filePath, "w")
    mon_fichier.write(str(len(slides))+"\n")
    for i in slides:
        if len(indice[i]) ==1:
            mon_fichier.write(str(indice[i][0])+"\n")
        else :
            mon_fichier.write(str(indice[i][0])+" " +str(indice[i][1])+"\n")

#print(lectureFichier("a_example.txt"))
slides =[0,2,1]
resultat, indice = lectureFichier("a_example.txt")
ecritureFichier("a_example_result.txt",slides,indice)
