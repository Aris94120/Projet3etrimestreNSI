from geopy.geocoders import Nominatim


def localisation(lieu):
    locator = Nominatim(user_agent='myGeocoder')
    location = locator.geocode(lieu)
    return location.latitude, location.longitude



"""
#GeoCoding : Fait de transformer une adresse en coordonnées GPS

#https://www.esri.com/training/catalog/59f8c6d71688630c7a5031d4/python-api%3A-search-for-an-address/


#Utilisation
latitude = localisation("Tour Eiffel Paris fr")[0] #Indiquez ici le lieu comme sur une recherche Google Maps
longitude = localisation("Tour Eiffel Paris fr")[1] #Indiquez ici le lieu comme sur une recherche Google Maps

print(latitude, longitude)
"""
Afficher = localisation(input("Entrez le lieu"))
print(Afficher)

