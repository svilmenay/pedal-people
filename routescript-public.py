import openrouteservice
import json

coords = []
distances = []
durations = []
elevations = []

client = openrouteservice.Client(key='5b3ce3597851110001cf624805cdb6f812d848939b729117991022c9') # Specify your personal API key

for i in coords:
    routes = client.directions(i,profile='cycling-regular',optimize_waypoints=True)
    distances.append(round(routes["routes"][0]["summary"]["distance"],2))
    durations.append(round(routes["routes"][0]["summary"]["duration"],2))
    
    estart = client.elevation_point(format_in='point',format_out='point',geometry=i[0])
    eend = client.elevation_point(format_in='point',format_out='point',geometry=i[len(i)-1])
    elevation = round((estart["geometry"][2]-eend["geometry"][2]),2)
    elevations.append(elevation)