

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# caricamento dataset
data = load_iris()

X = data.data
y = data.target

# standardizza le caratteristiche 
# richiama la classe StandardScaler e inizializza un oggetto assegnandolo alla v. sc
sc = StandardScaler()

# stima media del campione e deviazione standard e la standardizza
X_scaled = sc.fit_transform(X)

# suddivide i dati di train e di test (70/30)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# crea un modello ad albero decisionale addestrandolo sui dati di training
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# valutazione della performance del modello

# effettua le previsioni sui dati di test utilizzando il modello addestrato
y_pred = clf.predict(X_test)

# genera un report di classificazione con:
# precisione: previsione di proporzioni corrette per ogni classe
# richiamo: la capacità di catturare tutte le istanze di una certa classe
# F1-score: la media armonica di precisione e richiamo
# supporto: il numero di esempi effettivi di ogni classe
report = classification_report(y_test, y_pred, target_names=data.target_names)
print("Classification Report:\n", report)

# Calcola la matrice di confusione, che mostra quanti esempi di ciascuna classe sono stati previsti correttamente e quanti sono stati classificati erroneamente in altre classi
cm = confusion_matrix(y_test, y_pred)

# costruzione heatmap
plt.figure(figsize=(6,4))

# annot = 'True' visualizza i valori nelle celle della matrice
# fmt = 'd' formato in intero
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
 xticklabels=data.target_names, 
 yticklabels=data.target_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
