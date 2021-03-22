#Amaris Efthimou
#November 2019
#45 Collision Map

import folium
import pandas as pd

H = input("Enter CSV file name")
G = input("Enter output file")
th = pd.read_csv(H)
thMap = folium.Map(location=[40.768731,-73.964915])

for index,row in th.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["LOCATION"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(thMap)

thMap.save(outfile=G)
