
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

data = load_wine()

X = data.data
y = data.target

df = pd.DataFrame (data.data, columns=data.feature_names)

print(df.head())


plt.figure(figsize=(9, 7))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Matrice di Correlazione")
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# definizione del modello
rfc = RandomForestClassifier(random_state=42)

# definizione degli iperparametri
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 3, 5, 7],
    'criterion': ['gini', 'entropy']
    #'max_features': [None, 'srtq', 'log2', 'auto']
}

grid_search = GridSearchCV(estimator=rfc, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=1)
grid_search.fit(X_train, y_train)

print("Migliori iperparametri:", grid_search.best_params_)
# output: gini - max_depth: none - n_estimator: 50

# addestramento del modello sui dati di training
best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)

# valutazione sui dati di training
y_pred_train = best_model.predict(X_train)
accuracy_train = accuracy_score(y_train, y_pred_train)
print(f"Accuratezza sui dati di training: {accuracy_train}")

# metriche di valutazioni sui dati 
y_pred = best_model.predict(X_test)
accuracy_test = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print(f"Accuratezza sui dati di test: {accuracy_test}")
print(f"Precisione: {precision}")
print(f"Richiamo: {recall}")
print(f"F1-score: {f1}")

# matrice di confusione 
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=data.target_names, yticklabels=data.target_names)
plt.title("Matrice di Confusione")
plt.xlabel("Predetto")
plt.ylabel("Reale")
plt.show()

# report classificazione
report = classification_report(y_test, y_pred, target_names=data.target_names)
print(report)
