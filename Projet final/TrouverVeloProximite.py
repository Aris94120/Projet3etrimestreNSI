# -*- coding: utf-8 -*-
from math import cos, asin, sqrt
from CoordonneesCSV import StationDictionnaire, ListeAltitude1
from Localiser import localisation
import csv

fichier = open("BaseDeDonnees.csv")
contenu = csv.reader(fichier, delimiter=",")


def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))


def closest(data, v):
    return min(data, key=lambda p: distance(v['lat'], v['lon'], p['lat'], p['lon']))

def TrouverVeloProximite():
    adresse = input("Veuillez saisir votre adresse ou le lieux dit")  # Saisir ici votre adresse
    v = {'lat': localisation(adresse)[0], 'lon': localisation(adresse)[1]}
    StationPlusProcheGPS = closest(StationDictionnaire, v)
    # print(StationPlusProcheGPS)
    LigneStation = ListeAltitude1.index(StationPlusProcheGPS['lat'])  # Obtenir le numero de ligne du CSV des stations

    print("La station la plus proche de ce lieu est la suivante : ")

    c = 0
    for ligne in contenu:
        if c == LigneStation + 1:
            print("Numéro de la station:", ligne[0], "; place et ville:", ligne[1], ligne[13])
            print("Les coordonnées de cette stations sont :", ligne[11], ligne[12])
            print()
            print("Dans cette station, il reste:")
            print("Velo mécanique:", ligne[6])
            print("Velo électrique:", ligne[7])
            #print("Nombre de place pour restitution :", ligne[4])
        c += 1

'''
Source : https://stackoverflow.com/questions/41336756/find-the-closest-latitude-and-longitude
L'objectif de ce site était de pouvoir trouver parmis une liste de point, le point le plus proche du lieu voulu.
'''
