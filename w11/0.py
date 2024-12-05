import folium
from folium.folium import webbrowser

m = folium.Map(location=[48, 18])
m.save("map.html")
webbrowser.open("map.html")
