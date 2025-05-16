import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# Connessione al database
conn = sqlite3.connect("vendite.db")

# Query SQL con JOIN tra vendite e clienti
query = """
SELECT v.data,
       c.nome AS cliente,
       v.prodotto,
       v.quantità,
       v.prezzo_unitario,
       v.quantità * v.prezzo_unitario AS ricavo
FROM vendite v
JOIN clienti c ON v.cliente_id = c.id
"""

# Leggi il risultato in Pandas
df = pd.read_sql_query(query, conn)

# Chiudi la connessione
conn.close()

# Mostra i dati
print(df.head())

# Mostra il totale delle vendite per cliente
totale_vendite = df.groupby('cliente')['ricavo'].sum().reset_index()
totale_vendite.columns = ['cliente', 'totale_vendite']
print(totale_vendite)

# Mostra il totale delle vendite per prodotto
totale_prodotti = df.groupby('prodotto')['ricavo'].sum().reset_index()
totale_prodotti.columns = ['prodotto', 'totale_vendite']
print(totale_prodotti)

# Mostra il totale delle vendite per giorno
totale_giorni = df.groupby('data')['ricavo'].sum().reset_index()
totale_giorni.columns = ['data', 'totale_vendite']
print(totale_giorni)


# Ordinamento per miglior leggibilità
totale_vendite = totale_vendite.sort_values(by='totale_vendite', ascending=False)

# Plot
plt.figure(figsize=(8, 5))
plt.bar(totale_vendite['cliente'], totale_vendite['totale_vendite'])
plt.title("Ricavi per Cliente")
plt.xlabel("Cliente")
plt.ylabel("Totale Vendite (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_ricavi_clienti.png")
plt.show()

totale_prodotti = totale_prodotti.sort_values(by='totale_vendite', ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(totale_prodotti['prodotto'], totale_prodotti['totale_vendite'])
plt.title("Ricavi per Prodotto")
plt.xlabel("Prodotto")
plt.ylabel("Totale Vendite (€)")
plt.tight_layout()
plt.savefig("grafico_ricavi_prodotti.png")
plt.show()


totale_giorni['data'] = pd.to_datetime(totale_giorni['data'])

plt.figure(figsize=(8, 5))
plt.plot(totale_giorni['data'], totale_giorni['totale_vendite'], marker='o')
plt.title("Andamento Ricavi Giornalieri")
plt.xlabel("Data")
plt.ylabel("Totale Vendite (€)")
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_ricavi_temporali.png")
plt.show()