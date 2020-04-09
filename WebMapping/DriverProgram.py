#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The purpose of this project is to create a map of the world using the folium
package in python. The map will feature markers for the locations of volcanoes
in the USA that are color coordinated to signify the elevation in meters. Each
country is also color coordinated to signify the population it had as of 2005.
"""

import folium
import pandas

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'

if __name__ == "__main__":

    # Store data
    data = pandas.read_csv("Volcanoes.txt")

    # Store latitutde, longitude, and elevation respectively.
    lat = list(data['LAT'])
    lon = list(data['LON'])
    elev = list(data['ELEV'])

    # Initiate map
    map = folium.Map(location=[38.58, -99.09], zoom_start=6)
    # Initiate volcanoes feature group.
    fgv = folium.FeatureGroup(name="Volcanoes")
    # Add coordinates to volcanoes feature group.
    # The color implies the elevation. See color_producer function above. 
    for lt, ln, el  in zip(lat, lon, elev):
        fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el)+" m",
                                     color='grey', fill=True, fill_opacity=0.7,
                                     radius=6, fill_color=color_producer(el)))
     
    # Initiate the feature group for population
    fgp = folium.FeatureGroup(name="Population")
    # Apply colorful shade to countries based on color:.
    fgp.add_child(folium.GeoJson(data=(open('world.json', encoding='utf-8-sig').read()),
                                 style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                 else 'red'}))

    # add all folium children to map.
    map.add_child(fgv)
    map.add_child(fgp)
    map.add_child(folium.LayerControl())
    # save map
    map.save("Map1.html")