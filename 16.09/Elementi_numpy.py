
import numpy as np

# crea un array di numeri interi
arr = np.arange(10,50)
print(arr)

# cambia il tipo di dato
arr_float = arr.astype(np.float64)
print(arr_float.dtype)

# stampa la forma dell'array
print(arr_float.shape)

# genera 20 numeri casuali
array = np.random.randint(10, 51, size=20)

# estrae i primi 10 numeri
array_10 = array[:10]

# estrai gli ultimi 5 elementi
array_5 = array[-5:]

# estrai dal 5 al 15
array_5_15 = array[5:15]

# estrai ogni terzo elemento dell'array
array_passo_3 = array[::3]

# modifica gli elementi dall'indice 5 al 10 assegnando il valore 99
array[5:10] = 99

print("Array originale con modifiche:", array)
print("Primi 10 elementi:", array_10)
print("Ultimi 5 elementi:", array_5)
print("Elementi dall'indice 5 all'indice 15 (escluso):", array_5_15)
print("Ogni terzo elemento:", array_passo_3)

