
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# imposto un seed per la riproducibilità
np.random.seed(50)

# imposto i parametri
n_giorni = 365
n_medio_iniziale = 2000
n_medio_finale = 3000
std = 500
inizio_trend = 200
durata_trend = n_giorni - inizio_trend

# np.random.normal = genera una distribuzione normale con numeri causali (Fonte: La libreria di riferimento di Python )
# arrey di lunghezza 365, parametri: media, deviazione std, numeri casuali da generare)
visitatori = np.random.normal(loc = n_medio_iniziale, scale = std, size = n_giorni)

#Aggiunge una crescita lineare riempiendo l'array con 365 zero
crescita = np.zeros(n_giorni)

# Fonte (Chat GPT)
# [inizio trend] accede solo ai giorni in cui il trend sale
# [linspace] genera un array di valori che iniziano da 0 e arrivano a 1000 (3000 - 2000), 
# distribuiti uniformemente sulla durata del trend (dal giorno 200 al 365).
# 0 = da dove inizia il trend (sarebbe giorno 200); aumento desiderato (1000), numero di giorni in cui aumenta il trend (165) 
crescita[inizio_trend:] = np.linspace(0, n_medio_finale - n_medio_iniziale, durata_trend)

#somma dei trend di crescita: somma i due array. Numero di visitatori + l'aumento dopo il 200esimo giorno (trend di crescita) 
visitatori_crescita = visitatori + crescita

# genera una serie di dati partendo da 1 gennaio per una lunghezza di 365 giorni
date = pd.date_range(start= "2024-01-01", periods = n_giorni )

#creazione del dataframe con visitatori e dati
# la colonna del dataframe contiene i valori dell'array, l'indice è costruito con la serie di date
df = pd.DataFrame ({"Visitatori": visitatori_crescita}, index = date)

#resample = raggruppa i dati per intervalli mensili
#calcolo di media mensile e deviazione standard
media_mensile = df.resample("M").mean()
std_mensile = df.resample("M").std()


# Stampa dei risultati
print("Media mensile:\n", media_mensile)
print("\nDeviazione standard mensile:\n", std_mensile)

# Grafico della serie temporale, preso interamente con Chat GPT e riadattato aggiungendo i dati dell'esercizio
plt.figure(figsize=(10,6))
plt.plot(df.index, df['Visitatori'], label='Visitatori giornalieri con trend crescente')
plt.axvline(x=date[inizio_trend], color='r', linestyle='--', label='Giorno 200 (inizio crescita)')
plt.title("Simulazione di Visitatori Giornalieri in un Parco")
plt.xlabel("Data")
plt.ylabel("Numero di visitatori")
plt.legend()
plt.grid(True)
plt.show()