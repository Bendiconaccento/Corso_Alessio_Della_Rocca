
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#generazione della serie temporale 
giorni = pd.date_range(start = "2024-01-01", periods = 305)

#creazione di una normale con media 1200 e std 900
visitatori = np.random.normal(loc=1200, scale=900, size=305)

#diminuzione graduale del numero di visitatori
trend = np.linspace(0, -300, 305)

#aggiunge il trend decrescente al numero di visitatori
visitatori += trend

# assicura che i visitatori non siano negativi (Chat)
visitatori2 = np.clip(visitatori, 0, None).astype(int)

print(visitatori2)

# genera patologie casuali
patologie = np.random.choice(["ossa", "cuore", "testa"], size = 305)

# creazione dataframe
df = pd.DataFrame({
    "Data": giorni,
    "Visitatori": visitatori,
    "Patologia": patologie
})

print(df)

# imposta la colonna Data per effettuare l'operazione di resampling su base mensile e calcola su colonne specifice (mean,std) la media e la std dei visitatori 
df.set_index("Data", inplace=True)
df_mensile = df.resample("M").agg({
    "Visitatori" : ["mean", "std"]
})

print(f"Numero medio di visitatoiri per mese e deviazione standard: {df_mensile}")

# value_counts: restituisce una serie ordinata in ordine decrescente di frequenza
patologia_conta = df['Patologia'].value_counts()

#idmaxmax/min trova l'indice del valore massimo/minimo (Chat)
print("\nPatologia più comune:", patologia_conta.idxmax())
print("Patologia meno comune:", patologia_conta.idxmin())


# grafico a linee del numero di visitatori
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Visitatori'], label='Visitatori giornalieri')
plt.title('Numero di visitatori giornalieri')
plt.xlabel('Data')
plt.ylabel('Numero di visitatori')
plt.grid(True)

# aggiungi media mobile/ funzione .rolling window (Chat)
df['Media mobile 7 giorni'] = df['Visitatori'].rolling(window=7).mean()
plt.plot(df.index, df['Media mobile 7 giorni'], label='Media mobile (7 giorni)', color='orange')
plt.legend()
plt.show()

# grafico media mensile dei visitatori
df_mensile['Visitatori', 'mean'].plot(kind='bar', figsize=(10, 5), color='skyblue')
plt.title('Media mensile dei visitatori')
plt.xlabel('Mese')
plt.ylabel('Media dei visitatori')
plt.grid(True)
plt.show()

# grafico della distribuzione delle patologie
plt.figure(figsize=(8, 6))
patologia_conta.plot(kind='bar', color=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Distribuzione delle Patologie', fontsize=16)
plt.xlabel('Patologia')
plt.ylabel('Numero di Visitatori')
plt.show()