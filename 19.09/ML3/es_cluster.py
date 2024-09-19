
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.metrics import adjusted_rand_score, homogeneity_score

data = load_iris()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# trasformazione in df per visualizzazione dati
df = pd.DataFrame(data.data, columns=data.feature_names)
print(df.head())

# heatmap delle correlazioni tra le caratteristiche
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Matrice di Correlazione")
plt.show()

# pipeline con normalizzazione, PCA (riduzione delle dimensioni a 2 componenti), KMeans
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2)),
    ('kmeans', KMeans(n_clusters = 3, random_state = 42))
])

# applicazione della pipeline sui dati di training (addestramento)
pipeline.fit(X_train)

# predizione dei cluster per i dati di train e test
y_kmeans_train = pipeline.predict(X_train)
y_kmeans_test = pipeline.predict(X_test)

# riduce in in 2 le componenti principali i dati di training (sintassi: Chat)
X_pca_train = pipeline.named_steps['pca'].transform(X_train)

# scatterplot sulle componienti clusterizzati (Chat)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_pca_train[:, 0], y=X_pca_train[:, 1], hue=y_kmeans_train, palette='deep', s=100, alpha=0.6)
plt.title('KMeans Clustering con Pipeline (prime 2 componenti principali)')
plt.xlabel('Prima Componente Principale')
plt.ylabel('Seconda Componente Principale')
plt.show()

# valutazione del clustering
# misura la somiglianza tra i due cluster considerando quante coppie di campioni sono raggruppate allo stesso modo in entrambe le assegnazioni
# 1 / - 1 / 0 = corrispondenza casuale
ari = adjusted_rand_score(y_train, y_kmeans_train)

# misura quanto ciascun cluster contenga solo membri della stessa classe
# 1 = ogni cluster contiene solo campioni di una singola specie
# 0 = nessuna distinzione
homogeneity = homogeneity_score(y_train, y_kmeans_train)

print(f'Adjusted Rand Index (ARI): {ari:.3f}')
print(f'Homogeneity Score: {homogeneity:.3f}')

# mappatura tra Cluster Assegnati vs Specie Reali

# creazione di un df con etichette originali vs assegnate
df = pd.DataFrame({'Specie Reale': y_train, 'Cluster Assegnato': y_kmeans_train})

# questo passaggio ti consente di capire come l'algoritmo KMeans ha distribuito le osservazioni nei vari cluster 
# e di vedere quanto i cluster assegnati corrispondano alle specie reali di Iris. (Chat)
print("\nMappatura tra Cluster e Specie Reale:")
print(df.groupby(['Cluster Assegnato', 'Specie Reale']).size())