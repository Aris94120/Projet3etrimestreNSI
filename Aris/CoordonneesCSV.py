# -*- coding: utf-8 -*-
import csv

ListeAltitude = [] #Altitude
ListeLongitude = [] #Longitude
ListeAltitude1 = [] #Altitude
ListeLongitude1 = [] #Longitude
StationDictionnaire = []

with open("BaseDeDonnees.csv") as fichier:
    contenu = csv.reader(fichier, delimiter=",")
    for ligne in contenu:
        ListeAltitude.append(ligne[11])
    del ListeAltitude[0]
    for i in ListeAltitude:
        ListeAltitude1.append(float(i))

with open("BaseDeDonnees.csv") as fichier:
    contenu = csv.reader(fichier, delimiter=",")
    for ligne in contenu:
        ListeLongitude.append(ligne[12])
    del ListeLongitude[0]
    for i in ListeLongitude:
        ListeLongitude1.append(float(i))

'''
print(ListeAltitude1) #afficher altitude
print(ListeLongitude1) #afficher #longitude
'''

b = 0
for i in ListeAltitude1:
    StationDictionnaire.append({'lat':ListeAltitude1[b], 'lon':ListeLongitude1[b]})
    b+=1

'''
print(StationDictionnaire)
'''




