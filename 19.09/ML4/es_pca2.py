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

# 4. Applica PCA per ridurre i dati da 64 dimensioni a 2 dimensioni
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# 5. Visualizza i dati nel nuovo spazio bidimensionale, colorando i punti in base alla cifra rappresentata
plt.figure(figsize=(8, 6))
plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1], c=y_train, cmap='tab10', edgecolor='k', s=60, alpha=0.7)
plt.colorbar()
plt.title('PCA (prime 2 componenti) delle immagini di cifre')
plt.xlabel('Prima Componente Principale')
plt.ylabel('Seconda Componente Principale')
plt.show()

# addestra un modello di classificazione sui dati originali
clf_original = LogisticRegression(max_iter=10000)
clf_original.fit(X_train, y_train)

# prevedi sui dati di test originali
y_pred_original = clf_original.predict(X_test)
accuracy_original = accuracy_score(y_test, y_pred_original)
print(f"Lo score dei dati originali è: {accuracy_original}")

# addestra lo stesso modello utilizzando i dati ridotti con PCA
clf_pca = LogisticRegression(max_iter=10000)
clf_pca.fit(X_train_pca, y_train)

# prevedi sui dati di test ridotti con PCA
y_pred_pca = clf_pca.predict(X_test_pca)
accuracy_pca = accuracy_score(y_test, y_pred_pca)
print(f"Lo score dei dati ridotti è: {accuracy_pca}")

# lo score più basso dopo la riduzione delle dimenzioni sta a significare una perdita di informazioni: le due dimensioni non sono sufficienti a mantenere la separazione tra le classi rispetto a quelle originali.

