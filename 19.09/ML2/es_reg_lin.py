
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso


# caricamento dati
diabetes = load_diabetes()

X = diabetes.data
y = diabetes.target

# trasformazione in df per visualizzazione dati
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['progression'] = diabetes.target
print(df.head())

# distribuzione variaile target
sns.histplot(df['progression'], kde=True)
plt.title("Distribuzione della Progressione del Diabete")
plt.show()

# heatmap delle correlazioni tra le caratteristiche
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Matrice di Correlazione del Dataset Diabetes")
plt.show()

 # grafico a dispersione tra 1 caratteristica 'bmi' e la v. target
sns.scatterplot(x=df['bmi'], y=df['progression'])
plt.title("Relazione tra BMI e Progressione del Diabete")
plt.show()

# divisione dati
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# relazione tra caratteristiche e progressione del diabete
model = LinearRegression()

# aumento MSE e riduzione R^2
#model = Ridge(alpha=1.0)

# leggero miglioramento
#model = Lasso(alpha=0.1)

# addestramento dei dati di training
model.fit(X_train, y_train)

# valutazione della performance del modello
y_pred = model.predict(X_test)

# calcolo errore quadratico medio
mse = mean_squared_error(y_test, y_pred)

# calcolo coeff. di determinazione
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R^2 Score: {r2}")

# grafico a dispersione reali vs predetti
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # linea diagonale ideale
plt.xlabel('Valori Reali')
plt.ylabel('Valori Predetti')
plt.title('Valori Reali vs Predetti')
plt.show()