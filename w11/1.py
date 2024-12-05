import sqlite3.dbapi2 as sqlite

# vytvorenie spojenia a kurzora
conn = sqlite.connect("vzdelavanie.sqlite")
curs = conn.cursor()

"""sql
CREATE TABLE programy (
    id_programu INTEGER PRIMARY_KEY,
    nazov TEXT,
    forma TEXT, 
    stupen INTEGER
);
"""

curs.execute(
    # "CREATE TABLE programy (id_programu INTEGER PRIMARY_KEY, nazov TEXT, forma TEXT, stupen INTEGER);"
    "CREATE TABLE IF NOT EXISTS programy (id_programu INTEGER PRIMARY KEY, nazov TEXT, forma TEXT, stupen INTEGER);"
)

# curs.execute("INSERT INTO programy VALUES (120, 'informatika', 'denna', 1)")
# conn.commit()

pr = [
    (120, "informatika", "denná", 1),
    (121, "počítačové inžinierstvo", "denná", 1),
    (122, "manažment", "denná", 1),
    (123, "manažment", "externá", 1),
    (220, "informačné systémy", "denná", 2),
    (221, "počítačové inžinierstvo", "denná", 2),
    (232, "informačný manažment", "denná", 2),
    (233, "aplikované sieťové inžinierstvo", "denná", 2),
    (234, "inteligentné informačné systémy", "denná", 2),
    (235, "informačný manažment", "externá", 2),
]

# curs.executemany("INSERT INTO programy (id_programu, nazov, forma, stupen) VALUES (?, ?, ?, ?)", pr)
curs.executemany(
    "INSERT OR IGNORE INTO programy (id_programu, nazov, forma, stupen) VALUES (?, ?, ?, ?)",
    pr,
)
conn.commit()

curs.execute("SELECT * FROM programy")
out = curs.fetchall()
[print(i) for i in out]

curs.execute("SELECT nazov FROM programy WHERE stupen=1 and forma='denná'")
curs.fetchall()

curs.execute("SELECT stupen,COUNT(stupen) FROM programy GROUP BY stupen")
curs.fetchall()

"""
CREATE TABLE studenti(
    id_studenta INTEGER PRIMARY KEY,
    meno_studenta TEXT, 
    priezvisko TEXT NOT NULL, 
    rocnik INTEGER, 
    program INTEGER,
    FOREIGN KEY(PROGRAM) REFERENCES programy(id_programu)
);
"""

print("\n-------------------------\n")

curs.execute(
    """
    CREATE TABLE IF NOT EXISTS studenti(
        id_studenta INTEGER PRIMARY KEY,
        meno_studenta TEXT, 
        priezvisko TEXT NOT NULL, 
        rocnik INTEGER, 
        program INTEGER,
        FOREIGN KEY(program) REFERENCES programy(id_programu)
    );
    """
)

st = [
    (3791, "Peter", "Pan", 1, 120),
    (6134, "Jan", "Hrasko", 2, 120),
    (7543, "Lena", "Pysna", 1, 122),
    (5791, "Maria", "Kratka", 1, 123),
    (7410, "Jozef", "Mrkvicka", 1, 221),
    (9632, "Eva", "Benova", 2, 235),
]

curs.executemany(
    "INSERT OR IGNORE INTO studenti (id_studenta, meno_studenta, priezvisko, rocnik, program) VALUES (?, ?, ?, ?, ?)",
    st,
)
conn.commit()

curs.execute("SELECT * FROM studenti")
out = curs.fetchall()
[print(i) for i in out]

curs.execute("SELECT meno_studenta,priezvisko FROM studenti ORDER BY priezvisko")
out = curs.fetchall()
print()
[print(i) for i in out]

print("\n-------------------------\n")

curs.execute(
    "SELECT s.meno_studenta, s.priezvisko FROM studenti s, programy p WHERE p.nazov='informatika' AND s.program=p.id_programu"
)
out = curs.fetchall()
[print(i) for i in out]

print("\n-------------------------\n")

# studenti externeho studia
curs.execute(
    "SELECT s.meno_studenta, s.priezvisko FROM studenti s, programy p WHERE p.forma='externá' AND s.program=p.id_programu"
)
out = curs.fetchall()
[print(i) for i in out]

print("\n-------------------------\n")

# pocty studentov denneho bakalarskeho studia
curs.execute(
    "SELECT COUNT(s.id_studenta) FROM studenti s, programy p WHERE p.forma='denná' AND p.stupen=1 AND s.program=p.id_programu"
)
out = curs.fetchall()
[print(i) for i in out]

print("\n-------------------------\n")

# pocty studentov v jednolivych programoch externeho studia
curs.execute(
    "SELECT p.nazov, COUNT(s.id_studenta) FROM studenti s, programy p WHERE s.program=p.id_programu AND p.forma='externá' GROUP BY s.program"
)
[print(i) for i in curs.fetchall()]


print("\n------------------------------------------------")
print("UPRAVA UDAJOV")
print("------------------------------------------------\n")

# uprava
curs.execute("UPDATE studenti SET rocnik=3 WHERE priezvisko='Pan'")
curs.execute("SELECT * FROM studenti")
[print(i) for i in curs.fetchall()]

# vymazat studentov bakalarskeho studia  # nejak to nefunguje
curs.execute("DELETE FROM studenti WHERE program like '1%'")
curs.execute("SELECT * FROM studenti")
[print(i) for i in curs.fetchall()]


curs.close()
conn.close()
