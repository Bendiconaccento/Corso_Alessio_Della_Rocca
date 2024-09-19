
#classificazione supervisionata

# Importare le librerie necessarie
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.tree import plot_tree
import seaborn as sns
import matplotlib.pyplot as plt


# caricamento del dataset
data = load_wine()
X = data.data  
y = data.target  

#print(data)
#print(X)
#print(y)

# standardizzo le caratteristiche (x - media / std)
sc = StandardScaler()
X_scaled = sc.fit_transform(X)

# suddivisione dei dati in training (70%) e test set (30%)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)


# crea un modello ad albero decisionale addestrandolo sui dati di training
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# valutazione della performance del modello, genera un report
y_pred = clf.predict(X_test)
report = classification_report(y_test, y_pred, target_names=data.target_names)
print("Classification Report:\n", report)

# valutazione incrociata
scores = cross_val_score(clf, X_scaled, y, cv=5)
print(f"Accuracy (cross-validation): {scores}")

# accuratezza sui dati di addestramento  - (score simili, no overfitting)
train_accuracy = clf.score(X_train, y_train)

# accuratezza sui dati di test
test_accuracy = clf.score(X_test, y_test)

print(f"Training Accuracy: {train_accuracy:.2f}")
print(f"Test Accuracy: {test_accuracy:.2f}")

# visualizza l'albero decisionale (Chat)
#plt.figure(figsize=(12,8))
#plot_tree(clf, feature_names=data.feature_names, class_names=data.target_names, filled=True)
#plt.show()

# genera la matrice di confusione
cm = confusion_matrix(y_test, y_pred)

# visualizza la matrice di confusione
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
    xticklabels=data.target_names, 
    yticklabels=data.target_names)
plt.xlabel('Classe predetta')
plt.ylabel('Classe reale')
plt.title('Matrice di confusione')
plt.show()
