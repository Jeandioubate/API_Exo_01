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

# Récupération de "timestamp"
timestamp = data["timestamp"]

print()

# Affichage de "timestamp"
print("Timestamp :", timestamp)

# Conversion du timestamp en date
#
# datetime.datetime.fromtimestamp() transforme le timestamp en un objet datetime.
#
# "timestamp" représente le nombre de secondes écoulées depuis le 1er janvier 1970.
#
# datetime.timezone.utc indique que nous voulons obtenir la date et l'heure en UTC.

date_utc = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)

print()

# Affichage de la date et l'heure correspondant au timestamp
print("Date :", date_utc)

# Récupération des données concernant les personnes présentes actuellement dans l'espace
rep = requests.get(
    "http://api.open-notify.org/astros.json"
)

data_name = rep.json() # Conversion de la réponse JSON en dico Python

# Récupération du nombre d'occupants
number = data_name["number"]

print()

# Affichage du nombre d'occupants
print("Nombre d'occupants :", number)

# Récupération de la liste des personnes présentes dans l'espace
#
# ["people"] contient une liste de dictionnaires. Chaque dictionnaire correspond à une personne.
people = data_name["people"]

print()