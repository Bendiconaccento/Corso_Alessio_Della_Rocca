
import pandas as pd
import numpy as np
import random

nomi_maschili = ["Mirko","Aldo","Alessio","Giacomo","Maurizio"]
nomi_femminili = ["Martina","Francesca","Elena","Nicole","Chiara"]

città = ["Bologna","Roma","Bari","Cosenza","Pescara"]

# genera i dati da inserire nel df
def genera_persona():

    genere = random.choice(["Maschio","Femmina"])

    if genere == "Maschio":
        nome = random.choice(nomi_maschili)
    else:
        nome = random.choice(nomi_femminili)


    età = random.randint(10,99)
    residenza = random.choice(città)
    salario = random.randint(30000,100000)
    return [nome, età, residenza, salario]

# creazione del df con 12 righe
data = [genera_persona() for i in range(12)]
df = pd.DataFrame(data, columns=["Nome", "Età", "Città", "Salario"])

print(df)

# visualizza le prime e le ultime 5 righe
print(df.head())
print(df.tail())

# visualizza il tipo di dato di ciascuna colonna
print(df.dtypes)

# statistiche descrittive
print(df[["Età", "Salario"]].describe())

# identifica e rimuovere duplicati
#print(df.duplicated())
#df.drop_duplicates(inplace=True)

df = df.drop_duplicates()
df_cleaned = df.dropna()
print(df_cleaned)

# assegna in modo randomico gli na
# df.loc[] = accesso basato su etichette
df.loc[random.randint(0, 11), 'Età'] = np.nan
df.loc[random.randint(0, 11), 'Salario'] = np.nan

print(df)

# calcolare mediana e sostituzione degli na
mediana_età = df['Età'].median()
mediana_salario = df['Salario'].median()
df['Età'].fillna(mediana_età, inplace=True)
df['Salario'].fillna(mediana_salario, inplace=True)

print(df)


# aggiungere una nuova colonna "Categoria Età"
def categorizza_età(età):

    if età <= 18:
        return "Giovane"
    elif 19 <= età <= 65:
        return "Adulto"
    else:
        return "Senior"
    
df['Categoria Età'] = df['Età'].apply(categorizza_età)

print(df)

# salva il df pulito in un CSV
df.to_csv("Esercizio_1.csv", index = False)