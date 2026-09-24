import requests
import datetime

"""
Ce programme récupère des informations concernant la Station Spatiale
Internationale (ISS) à partir de l'API Open Notify.

Le programme affiche :
- la latitude de l'ISS ;
- la longitude de l'ISS ;
- le timestamp correspondant à sa position ;
- la date et l'heure correspondant au timestamp ;
- le nombre de personnes actuellement dans l'espace ;
- le nom de chaque occupant.
"""

# Récupération des données sur la position de la station spatiale internationale (ISS)
# requests.get() envoie une requête HTTP GET à l'API. L'API va nous retourner les informations concernant
# la position actuelle de l'ISS.
response = requests.get(
    "http://api.open-notify.org/iss-now.json"
)

# Conversion de la réponse JSON de l'API en dictionnaire Python.
data = response.json()

print("=== STATION SPATIALE INTERNATIONALE ===")
print()
print("Position de l'ISS :")

# Récupération de la latitude et de la longitude
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

# Affichage de la latitude et de la longitude
print("Latitude :", latitude)
print("Longitude :", longitude)