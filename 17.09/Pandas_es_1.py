
import pandas as pd


# genera un mese di date
date = pd.date_range(start="2024-09-01", periods = 30)
print(date)

# dati e df

città = ["Bologna", "Roma", "Napoli"] * 10
prodotti = ["Tortellini", "Carbonara", "Pizza"] * 10
vendite = [
    100, 150, 200, 250, 300, 350, 400, 450, 500, 550,
    120, 170, 220, 270, 320, 370, 420, 470, 520, 570,
    130, 180, 230, 280, 330, 380, 430, 480, 530, 580
]

dati = {
    "Date": date,
    "Città": città,
    "Prodotto": prodotti,
    "Vendite": vendite
}

df = pd.DataFrame(dati)

print(df)

# creazione tabella pivot
pivot_df = df.pivot_table(values = "Vendite", index = "Prodotto", columns = "Città", aggfunc = "mean")
print(pivot_df)

# creazione tabella grouped by
grouped_df = df.groupby("Prodotto")["Vendite"].sum()
print(grouped_df)