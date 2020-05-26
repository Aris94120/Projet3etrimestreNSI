# -*- coding: utf-8 -*-
import csv

from Localiser import localisation
from CoordonneesCSV import ListeLongitude1, ListeAltitude1

a = 1000000000000  # pour avoir nombre entier
stationsAltitude = []
stationsLongitude = []

"""
https://www.geeksforgeeks.org/python-find-closest-number-to-k-in-given-list/
Tout les print sous forme de commentaire sont là pour aider le debeugage du programme
"""

adresse = "27 rue des beaumonts 94120"  # Entrez l'adresse
positionAltitude = localisation(adresse)[0]
positionLongitude = localisation(adresse)[1]
print(positionAltitude)
print(positionLongitude)

for i in ListeAltitude1:
    stationsAltitude.append(round(i*a))

for i in ListeLongitude1:
    stationsLongitude.append(round(i*a))

#print(ListeAltitude1)
#print(ListeLongitude1)

StationProcheAltitude = min(stationsAltitude, key=lambda x: abs(x - positionAltitude))
print(StationProcheAltitude)

StationProcheLongitude = min(stationsLongitude, key=lambda x: abs(x - positionLongitude))
#print(StationProcheLongitude)


#print(stationsAltitude.index(StationProcheAltitude))
#print(stationsLongitude.index(StationProcheLongitude))

"""
for i in stations:
    if StationProche == 5130947554993:
        #print("Bonjour")

"""
