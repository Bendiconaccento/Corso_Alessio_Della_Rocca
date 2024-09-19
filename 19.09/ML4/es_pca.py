
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

digits = load_digits()

X = digits.data
y = digits.target

# esplorazione dati
print("Shape dei dati:", digits.data.shape)  
print("Target:", np.unique(digits.target))

# visualizza alcune immagini di esempio dal dataset (Chat)
plt.figure(figsize=(10, 4))
for i in range(10):
    plt.subplot(2, 5, i + 1)    # dispone 10 immagini su una singola riga
    plt.imshow(digits.images[i], cmap='gray')   # scala di grigi per i pixel  di ogni elemento
    plt.title(f'Cifra: {digits.target[i]}')
    plt.axis('off')
plt.show()

# divisione train test 80/20
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('scaler', StandardScaler()),  # normalizzazione dati
    ('pca', PCA(n_components=2, whiten=True)),  # riduzione a 2 componenti
    ('classifier', LogisticRegression(max_iter=10000))  # regressione logistica
])

# addestramento sui dati di training
pipeline.fit(X_train, y_train)

# previsione su dati non etichettati
y_pred = pipeline.predict(X_test)

# valutazione delle performance
print(classification_report(y_test, y_pred))

accurancy = accuracy_score(y_test, y_pred)
print(f"Lo score dopo la PCA e la regressione è: {accurancy}")

#DIAGNOSTICA (possibile problema di underfitting: basse performance su entrambi i set)
y_pred_train = pipeline.predict(X_train)
accuracy_train = accuracy_score(y_train, y_pred_train)
print(f"Accuratezza sui dati di training: {accuracy_train}")

# riduce a 2 le componenti principali i dati di training e normalizza (sintassi: Chat)
X_train_pca = pipeline.named_steps['pca'].transform(pipeline.named_steps['scaler'].transform(X_train))

# scatterplot sulle componienti con seaborn (Chat)
plt.figure(figsize=(8, 6))
# hue = coloro i punti del grafico con la sua etichetta
# tabe10 = palette di 10 colori distinti
# s = 60 dimensioni dei punti
# trasparenza dei punti (1 = meno trasparenti)
sns.scatterplot(x=X_train_pca[:, 0], y=X_train_pca[:, 1], hue=y_train, palette='tab10', s=60, alpha=0.7)
plt.title('Dati ridotti con PCA (prime 2 componenti)')
plt.xlabel('Prima Componente Principale')
plt.ylabel('Seconda Componente Principale')
plt.show()

# i punti di diverse classi si sovrappongono, sembra che le due componenti principali 
# non sono sono sufficienti per catturare tutta la variabilità necessaria per separare bene le classi.


# prova con i dati di test (20%) non cambia (come confermato dai risultati delle performance)

X_test_pca = pipeline.named_steps['pca'].transform(pipeline.named_steps['scaler'].transform(X_test))

plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_test_pca[:, 0], y=X_test_pca[:, 1], hue=y_test, palette='tab10', s=60, alpha=0.7)
plt.title('Dati ridotti con PCA (prime 2 componenti)')
plt.xlabel('Prima Componente Principale')
plt.ylabel('Seconda Componente Principale')
plt.show()



