import json
import requests
import os
import proxy_lib
import folium
import pandas as pd

lime = {'fillColor': '#00FF00', 'color': '#00FF00'}
green = {'fillColor': '#99ff00', 'color': '#99ff00'}
yellow = {'fillColor': '#FFCC00', 'color': '#FFCC00'}
gold = {'fillColor': '#ff6600', 'color': '#ff6600'}
orange = {'fillColor': '#FF3300', 'color': '#FF3300'}
red = {'fillColor': '#FF0000', 'color': '#FF0000'}


f = open("AQMO-UR1_50~200_bus_all_2020-02-29T23-00-00.000Z_step_year.geojson","r")
geojson_air = f.read()
gjpc = json.loads(geojson_air)
f.close()

g = open("pistes_cyclables.geojson","r")
geojson_pistes_cyclables = g.read()
pistes = json.loads(geojson_pistes_cyclables)
g.close()

carte = folium.Map(location=[ 48.116622, -1.638717],zoom_start=12)
style2 = {'fillColor': '#595552', 'color': '#595552'}
folium.GeoJson(pistes, name="Pistes Cyclables",style_function=lambda x:style2).add_to(carte)

areas = len(gjpc['features'])
o = 0
while o < areas:
    average = gjpc['features'][o]['properties']["avg"]
    if average <= 2 and average > 0:
        folium.GeoJson(gjpc['features'][o], name="Qualité de l'air",style_function=lambda x:lime).add_to(carte)
    if average <= 4 and average > 2:
        folium.GeoJson(gjpc['features'][o], name="Qualité de l'air",style_function=lambda x:green).add_to(carte)
    if average <= 6 and average > 4:
        folium.GeoJson(gjpc['features'][o], name="Qualité de l'air",style_function=lambda x:yellow).add_to(carte)
    if average <= 8 and average > 6:
        folium.GeoJson(gjpc['features'][o], name="Qualité de l'air",style_function=lambda x:gold).add_to(carte)
    if average <= 10 and average > 8 :
        folium.GeoJson(gjpc['features'][o], name="Qualité de l'air",style_function=lambda x:orange).add_to(carte)
    if average > 10 :
        folium.GeoJson(gjpc['features'][o], name="Qualité de l'air",style_function=lambda x:red).add_to(carte)
    maxi = gjpc['features'][o]['properties']["max"]
    o += 1
    if maxi > 40:
        maxi = 40  
carte
carte.save("carte.html")      



        
        
    
        