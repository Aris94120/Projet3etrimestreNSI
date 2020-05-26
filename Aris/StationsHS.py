# -*- coding: utf-8 -*-
import csv

def StationsHS():
    fichier = open("BaseDeDonnees.csv")
    contenu = csv.reader(fichier, delimiter=",")
    print("Les stations hors services sont les suivantes:")
    for ligne in contenu:
        if ligne[2] == "NON":
            print("Numéro de la station:",ligne[0],"; place et ville:",ligne[1],ligne[13])
