import requests
import os
import json
import proxy_lib

data_set_local_id = "amenagements-velo-et-zones-de-circulation-apaisee"
if  not proxy_lib.download(data_set_local_id,"application/geo+json","pistes_cyclables.geojson"):
    print("Le téléchargement de "+data_set_local_id+" a échoué")

