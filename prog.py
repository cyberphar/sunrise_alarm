#!/usr/bin/env python

import colorsys
from time import sleep, time as tm
import sys

# import blinkt

from datetime import time, datetime, timedelta

# lever soleil
import ephem

# Coordonnées géographiques de votre emplacement
latitude = '48.8566'  # Latitude de Paris
longitude = '2.3522'  # Longitude de Paris

# Création de l'objet observer avec les coordonnées géographiques
observer = ephem.Observer()
observer.lat = latitude
observer.lon = longitude

# Utilisation de la date actuelle pour calculer l'heure du lever du soleil
observer.date = datetime.utcnow()

# Calcul de l'heure du lever du soleil
sunrise_time = observer.next_rising(ephem.Sun()).datetime()

sunrise_time = sunrise_time + timedelta(hours=2)

# Affichage de l'heure du lever du soleil
print("Lever du soleil :", sunrise_time.time())





try:
    hour1 = int(sys.argv[1])
    min1 = int(sys.argv[2])
    hour2 = int(sys.argv[3])
    min2 = int(sys.argv[4])
except Exception as e:
    print(e)
    hour1 = sunrise_time.hour
    min1 = sunrise_time.minute
    if min1 >= 50:
        hour2 = hour1 + 1
        min2 = (min1 + 10)%60
    else:
        hour2 = hour1
        min2 = min1 + 10

heure_debut = time(hour1, min1, second=0, microsecond=0)
heure_fin = time(hour2, min2, second=0, microsecond=0)

difference_minutes = (heure_fin.minute - heure_debut.minute) % 60

heure_actuelle = datetime.now().time()

spacing = 360.0 / 16.0
hue = 0

# blinkt.set_clear_on_exit()

brightness = 0.1
# blinkt.set_brightness(brightness)

def nombre_total_secondes(temps1, temps2):
    secondes1 = temps1.hour * 3600 + temps1.minute * 60 + temps1.second
    secondes2 = temps2.hour * 3600 + temps2.minute * 60 + temps2.second
    return abs(secondes2 - secondes1)


while heure_actuelle >= heure_debut and heure_actuelle <= heure_fin:
    '''
    hue = int(tm.time() * 100) % 360
    for x in range(blinkt.NUM_PIXELS):
        offset = x * spacing
        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        blinkt.set_pixel(x, r, g, b)

    blinkt.show()
    '''
    sleep(0.001)
    heure_actuelle = datetime.now().time()

    # Calcul de la différence de temps en secondes
    difference = nombre_total_secondes(datetime.now(), heure_debut)

    if brightness != 1.0:
        brightness = round(round(difference)/(0.75*nombre_total_secondes(heure_fin, heure_debut)),3)
        print(brightness)
        # blinkt.set_brightness(brightness)
