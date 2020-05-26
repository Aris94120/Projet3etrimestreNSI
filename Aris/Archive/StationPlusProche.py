# -*- coding: utf-8 -*-
import csv
import numpy as np
from Localiser import localisation
from CoordonneesCSV import ListeLongitude1, ListeAltitude1

a = 100000000000
ListeLongitude2 = []
ListeAltitude2 = []

adresse = "27 rue des beaumonts 94120"  # Entrez l'adresse

position1 = (round(a * localisation(adresse)[0]))
position2 = (round(a * localisation(adresse)[1]))


for i in ListeLongitude1:
    ListeLongitude2.append(round(a * i))
#print(ListeLongitude2)
for i in ListeAltitude1:
    ListeAltitude2.append(round(a * i))
#print(ListeAltitude2)

# https://www.geeksforgeeks.org/python-find-closest-number-to-k-in-given-list/

# Python3 program to find Closest number in a list

StationAltitude = min(ListeAltitude2, key=lambda x:abs(x-position1))
print(StationAltitude/a)

StationLongitude = min(ListeLongitude2, key=lambda x:abs(x-position2))
print(StationLongitude/a)

"""
Nouvelle idée : prendre deux coordonnées les multipliés entre elle et trouver les données les plus proches
"""
