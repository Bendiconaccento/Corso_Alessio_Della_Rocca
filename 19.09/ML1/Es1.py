
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from scipy.stats import randint as sp_randint
from scipy.stats import uniform



# caricamento del dataset
data = load_wine()
X = data.data
y = data.target

# suddivisione dei dati in training (80%) e test set (20%)
# stratify: mantiene la proporzione delle classi nei set di train e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


# creazione della pipeline per concatenare vari step. E' un oggetto, salva i dati.
# standardizzazione; riduzione dimensionalità; classificatore boosting: ddestra il modello in sequenza e ogni nuovo modello cerca di correggere il modello precedente (geeksforgeeks)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA()),
    ('gbc', GradientBoostingClassifier(random_state = 42))
])

# definizione dello spazio di ricerca degli iperparametri
param_distributions = {
    
    # prova diverse quantità di componenti principali
    'pca__n_components': sp_randint(5, 13),
    # numero di alberi del gradient boosting
    'gbc__n_estimators': sp_randint(50, 200),
    # tasso di apprendimento per il boosting
    'gbc__learning_rate': uniform(0.01, 0.2),
    # profondità massima degli alberi
    'gbc__max_depth': sp_randint(1, 5),
    # frazionamento del dataset. <1 introduce casualità nel processo di addestramento (riduce l'overfitting)
    'gbc__subsample': uniform(0.6, 0.4),
    # specifica il numero minimo di campioni rihiesti per dividere un nodo. Un valore alto impedisce di fare lo split con pochi campioni (riduce overfitting)
    'gbc__min_samples_split': sp_randint(2, 10),
    # definisce il numero minimo di campioni richiesti per essere un nodo terminale
    'gbc__min_samples_leaf': sp_randint(1, 10),
    # determina quanti e quali attributi del dataset sono considerati per ogni split (limita il numero di caratteristiche utilizzate in ogni split, migliorando l'efficienza e la capacità di generalizzazione)
    'gbc__max_features': ['auto', 'sqrt', 'log2', None]

}

# crea suddivisioni che mantengono la proporzione delle classi nel set di dati
# n_split : numero di campioni per dividere un nodo
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# invece di testare tutte le combinazioni di parametri (come fa GridSearchCV), esplora casualmente una serie di possibili valori
# param_dist : dizionario dei parametri da cercare
# n_iter = 50 : numero di combinazioni casuali da provare
# cv : metodo di validazione incrociata
# scoring: metrica per valutare le prestazioni
# n_jobs = -1 : utilizza tutti i processori disponibili
random_search = RandomizedSearchCV(pipeline, param_distributions=param_distributions, 
                                   n_iter=50, cv=cv, scoring = 'accuracy', n_jobs=-1, random_state=42)

# addestramento 
random_search.fit(X_train, y_train)

# estrae il miglior modello della ricerca casuale
best_model = random_search.best_estimator_
print(f"Migliori parametri trovati: {best_model}")

# valutazione del modello
y_pred = random_search.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza sul test set: {accuracy:.4f}")

report = classification_report(y_test, y_pred)
print(f"Report di classificazione: {report}")

conf_matrix = confusion_matrix(y_test, y_pred)
print(f"Matrice di confusione: {conf_matrix}")

# visualizza la matrice di confusione
plt.figure(figsize=(6,4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
    xticklabels=data.target_names, 
    yticklabels=data.target_names)
plt.xlabel('Classe predetta')
plt.ylabel('Classe reale')
plt.title('Matrice di confusione')
plt.show()

