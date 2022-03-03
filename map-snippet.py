import requests
import os
import folium

carte = folium.Map(location=[ 48.116622, -1.638717],zoom_start=12)
carte.save("carte.html")

