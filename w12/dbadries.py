import sqlite3.dbapi2 as sqlite
import folium
from numpy import mean

conn = sqlite.connect("adresy.sqlite")
curs = conn.cursor()

curs.execute("CREATE TABLE IF NOT EXISTS obce(id_obce INTEGER PRIMARY KEY,nazov_obce TEXT);")
curs.execute("CREATE TABLE IF NOT EXISTS ulice(id_ulice INTEGER PRIMARY KEY,nazov_ulice TEXT,id_obce INTEGER,foreign key(id_obce) references obce(id_obce));")
curs.execute("CREATE TABLE IF NOT EXISTS cisla(id_domu INTEGER PRIMARY KEY,cislo_domu TEXT,latitude INTEGER, longtitude INTEGER, id_ulice INTEGER,foreign key(id_ulice) references obce(id_ulice));")

with open("obce.csv") as f:
    for riadok in f:
        oid,omeno=riadok[:-1].split(",")
        curs.execute("INSERT OR IGNORE INTO obce VALUES (?,?)", (int(oid), omeno))

with open("ulice.csv") as f:
    for riadok in f:
        uid,umeno,oid=riadok[:-1].split(",")
        curs.execute("INSERT OR IGNORE INTO ulice VALUES (?,?,?)", (int(uid), umeno, int(oid)))

with open("cisla.csv") as f:
    for riadok in f:
        did,cd,lat,lon,uid=riadok[:-1].split(",")
        curs.execute("INSERT OR IGNORE INTO cisla VALUES (?,?,?,?,?)", (int(did), cd, lat, lon, int(uid)))

def lokalizacia_ulice(ulica, mesto):
    curs.execute("SELECT c.cislo_domu,latitude,longtitude FROM cisla c,ulice u,obce o WHERE o.nazov_obce LIKE '%" + mesto + "%' AND o.id_obce = u.id_obce AND u.nazov_ulice LIKE '%" + ulica + "%' AND u.id_ulice = c.id_ulice GROUP BY cislo_domu")
    return curs.fetchall()

def lokalizacia_adresy(ulica, cislo, mesto):
    curs.execute("SELECT c.cislo_domu,latitude,longtitude FROM cisla c,ulice u,obce o WHERE o.nazov_obce LIKE '%" + mesto + "%' AND o.id_obce = u.id_obce AND u.nazov_ulice LIKE '%" + ulica + "%' AND u.id_ulice = c.id_ulice AND c.cislo_domu LIKE '%" + cislo + "%'")
    return curs.fetchall()

print(lokalizacia_ulice("Univerzitná", "Žilina"))
print(lokalizacia_adresy("Farského", "12", "Bratislava"))
print()

ulica = "Bojnická"
mesto = "Prievidza"
r = lokalizacia_ulice(ulica, mesto)

# mesto = "Prešov"
# r = lokalizacia_ulice(ulica, )

C,Lat,Lon = zip(*r)
sur = zip(Lat,Lon)
Lats,Lons = mean(Lat), mean(Lon)

map = folium.Map(location=(Lats, Lons), zoom_start=17)
for p,c in zip(sur,C):
    map.add_child(folium.CircleMarker(p, radius=6, color="red", fill_color="red", fill_opacity=0.3, popup=f"{ulica}, {c}"))

map.save("final_map.html")
map.show_in_browser()

