import requests
import os
import json
import proxy_lib
import folium

data_set_local_id = "amenagements-velo-et-zones-de-circulation-apaisee"
if  not proxy_lib.download(data_set_local_id,"application/geo+json","pistes_cyclables.geojson"):
    print("Le téléchargement de "+data_set_local_id+" a échoué")

f = open("pistes_cyclables.geojson","r")
geojson_pistes_cyclables = f.read()
gjpc = json.loads(geojson_pistes_cyclables)

f.close()

carte = folium.Map(location=[ 48.116622, -1.638717],zoom_start=12)
style1 = {'fillColor': '#228B22', 'color': '#228B22'}
folium.GeoJson(gjpc, name="Pistes Cyclables",style_function=lambda x:style1).add_to(carte)

