import json
import requests
import os
import proxy_lib
import folium
import pandas as pd
from shapely.geometry import Point, Polygon
from shapely.geometry import LineString, MultiLineString

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

areas = len(gjpc['features'])
n_pistes=len(pistes["features"])

j=0
i=0
o=0
k=0

while o < areas:
    average = gjpc['features'][o]['properties']["avg"]
    if average > 10 :
        coordinates = gjpc["features"][o]["geometry"]["coordinates"][0]
        poly=Polygon(coordinates)
        for i in range(n_pistes):
            data_piste = pistes["features"][i]
            if data_piste is not None:
                geometry = pistes["features"][i]["geometry"]
                if geometry is not None:
                    coordenada = pistes["features"][i]["geometry"]["coordinates"]
                    piste=LineString(coordenada)
                    if poly.intersects(piste):
                        folium.GeoJson(piste, name="Qualité de l'air",style_function=lambda x:red).add_to(carte)
    maxi = gjpc['features'][o]['properties']["max"]
    o += 1
    if maxi > 40:
        maxi = 40  
carte
carte.save("intersect.html")      



        
        
    
        