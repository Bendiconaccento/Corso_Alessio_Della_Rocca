
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#plt.rcParams['figure.figsize'] = [10, 6]
# Imposta la dimensione predefinita delle figure

#plt.rcParams['figure.dpi'] = 100
# Imposta la risoluzione delle figure in DPI

#plt.rcParams['figure.facecolor'] = 'white' 
# Colore di sfondo della figura

#Configura Seaborn
sns.set_theme(style="darkgrid")

# Crea alcuni dati
data = np.random.normal(size=100)

# Crea un grafico
sns.histplot(data, kde=True)
plt.title('Distribuzione dei dati')
plt.show()