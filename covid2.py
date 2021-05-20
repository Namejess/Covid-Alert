# -*- coding: utf-8 -*-
from pprint import pprint
import requests
import json, os, time, sys

def get_centre():
    url = "https://vitemadose.gitlab.io/vitemadose/54.json"
    r = requests.get(url)   
    centre_disponible = r.json().get("centres_disponibles", [])

    for centre in centre_disponible : 
        url_centre =  centre.get("url")
        location =    centre.get("location", [])
        for locations in location:
            city = location.get("city", "")
            if city != "Vandœuvre-lès-Nancy":
                continue
            
            print(url_centre)

    return centre
    
if __name__ == "__main__":
    while True: 
        get_centre()
        print("Attendre 5m")
        time.sleep(300)
