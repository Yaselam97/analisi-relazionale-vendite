import sqlite3

# Connessione (crea il file vendite.db)
conn = sqlite3.connect("vendite.db")
cursor = conn.cursor()

# Carica ed esegue lo script SQL
with open("db_vendite.sql", "r", encoding="utf-8") as file:
    sql_script = file.read()
    cursor.executescript(sql_script)

conn.commit()
conn.close()

print("✅ Database creato correttamente!")
