import sqlite3.dbapi2 as sqlite

conn = sqlite.connect("adresy.sqlite")
curs = conn.cursor()

curs.execute("CREATE TABLE IF NOT EXISTS obce (id_obce INTEGER PRIMARY KEY, nazov_obce TEXT)")
curs.execute("CREATE TABLE IF NOT EXISTS ulice (id_ulice INTEGER PRIMARY KEY, nazov_ulice TEXT, id_obce INTEGER, FOREIGN KEY(id_obce) REFERENCES obce(id_obce))")
curs.execute("CREATE TABLE IF NOT EXISTS cisla (id_domu INTEGER PRIMARY KEY, cislo_domu TEXT, lat INTEGER, lon INTEGER, id_ulice INTEGER, FOREIGN KEY(id_ulice) REFERENCES ulice(id_ulice))")

with open("obce.csv", "r") as file:
    for line in file:
        o_id, o_nazov = line[:-1].split(",")
        try:
            curs.execute("INSERT OR IGNORE INTO obce (id_obce, nazov_obce) VALUES (?,?)", (int(o_id), o_nazov))
        except sqlite.IntegrityError:
            pass

with open("ulice.csv", "r") as file:
    for line in file:
        u_id, u_nazov, o_id = line[:-1].split(",")
        try:
            curs.execute("INSERT OR IGNORE INTO ulice (id_ulice, nazov_ulice, id_obce) VALUES (?,?,?)", (int(u_id), u_nazov, int(o_id)))
        except sqlite.IntegrityError:
            pass

with open("cisla.csv", "r") as file:
    for line in file:
        id_domu, cislo_domu, lat, lon, id_ulice = line[:-1].split(",")
        try:
            curs.execute("INSERT OR IGNORE INTO cisla (id_domu, cislo_domu, lat, lon, id_ulice) VALUES (?,?,?,?,?)", (int(id_domu), cislo_domu, float(lat), float(lon), int(id_ulice)))
        except sqlite.IntegrityError:
            pass

# zoznam vsetkych ulic v ziline
curs.execute("SELECT u.nazov_ulice FROM obce o, ulice u WHERE o.nazov_obce='Žilina' AND u.id_obce=o.id_obce")
[print(i) for i in curs.fetchall()]

# pocet vsetkych ulic v bratislave
curs.execute("SELECT COUNT(u.nazov_ulice) FROM obce o, ulice u WHERE o.nazov_obce LIKE 'Bratislava%' AND u.id_obce=o.id_obce")
[print(i) for i in curs.fetchall()]

# pocet vsetkych cisel na ulici univerzitna v ziline
curs.execute("SELECT COUNT(c.id_domu) FROM obce o, ulice u, cisla c WHERE o.nazov_obce='Žilina' AND u.nazov_ulice='Univerzitná' AND u.id_obce=o.id_obce AND c.id_ulice=u.id_ulice")
[print(i) for i in curs.fetchall()]

# zoznam vsetkych cisel na ulici univerzitna v ziline a ich suradnice
curs.execute("SELECT c.id_domu, c.lat, c.lon FROM obce o, ulice u, cisla c WHERE o.nazov_obce='Žilina' AND u.nazov_ulice='Univerzitná' AND u.id_obce=o.id_obce AND c.id_ulice=u.id_ulice")
[print(i) for i in curs.fetchall()]
  
