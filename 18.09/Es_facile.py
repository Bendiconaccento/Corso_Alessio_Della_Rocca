

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import random

temperatura = np.random.randint(-10, 7, size = 31)
df = pd.DataFrame(temperatura, columns=["Temperatura giornaliera"])

print(df)

temp_max = df["Temperatura giornaliera"].max()
temp_min = df["Temperatura giornaliera"].min()
temp_mean = df["Temperatura giornaliera"].mean()
temp_median = df["Temperatura giornaliera"].median()

print(f"La temperatura massima è {temp_max}")
print(f"La temperatura minima è {temp_min}")
print(f"La temperatura media è {temp_mean}")
print(f"La temperatura mediana è {temp_median}")


plt.figure(figsize=(10,6))

plt.plot(df["Temperatura giornaliera"], marker='o', linestyle='-', color='blue', label='Temperature giornaliere')
plt.title("Temperature giornaliere")
plt.xlabel("Giorni mese di gennaio")
plt.ylabel("Temperatura (C°)")

#Dettagli chiesti a Chat
plt.axhline(y=temp_max, color='red', linestyle='--', label=f'Temperatura massima ({temp_max:.2f}°C)')
plt.axhline(y=temp_min, color='green', linestyle='--', label=f'Temperatura minima ({temp_min:.2f}°C)')
plt.axhline(y=temp_mean, color='orange', linestyle='--', label=f'Temperatura media ({temp_mean:.2f}°C)')
plt.axhline(y=temp_median, color='purple', linestyle='--', label=f'Mediana ({temp_median:.2f}°C)')

plt.legend()
plt.grid(True)

plt.show()