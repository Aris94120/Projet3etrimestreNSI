from sys import *
from TrouverVeloProximite import TrouverVeloProximite
from StationsHS import StationsHS
from Forfait import Forfait
from Parking import Parking

def menu():
    print("-----------------------------------")
    print("1- Trouver un vélo")
    print("2- Trouver une place de parking")
    print("3- Voir les stations HS")
    print("4- Accéder à la liste des stations de votre ville")
    print("5- Voir les tarifs")
    print("6- Quitter\n")

    ActionUtilisateur1 = int(
        input("Merci de bien vouloir entrez le chiffre du programme que vous-voulez lancer, ex : 1"))
    print("-----------------------------------")

    if ActionUtilisateur1 == 1:
        TrouverVeloProximite()
        input("Veuiller appuyer sur une touche pour revenir au menu")
        menu()
    if ActionUtilisateur1 == 2:
        Parking()
        input("Veuiller appuyer sur une touche pour revenir au menu")
        menu()
    if ActionUtilisateur1 == 3:
        StationsHS()
        input("Veuiller appuyer sur une touche pour revenir au menu")
        menu()
    if ActionUtilisateur1 == 4:
        print("ERREUR: Fonction toujours en développement, appuyer sur 'A puis enter'")
        input("Veuiller appuyer sur une touche pour revenir au menu")
        menu()
    if ActionUtilisateur1 == 5:
        Forfait()
        input("Veuiller appuyer sur une touche pour revenir au menu")
        menu()
    if ActionUtilisateur1 == 6:
        print("Le programme va se quitter")
        exit()
    else:
        print("\nCette fonctionalité n'existe pas !")
        print("Retour au menu principal")
        menu()


print("Bienvenue dans votre nouvelle application Velib' métropole")
menu()
