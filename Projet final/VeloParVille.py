import csv

def VeloParVille():
    fichier = open("BaseDeDonnees.csv")
    contenu = csv.reader(fichier, delimiter=",")
    v=input("Veuillez indiquer votre ville.")
    print("----------------------------------------------")
    print("Les stations disponibles dans votre villes sont les suivantes:")
    for ligne in contenu:
        if v==ligne[13] :
            print("Numéro de la station:",ligne[0],"; place et ville:",ligne[1],ligne[13])
