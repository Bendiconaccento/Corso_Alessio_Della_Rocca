

#Creare 2 script:
#1) genera 5 numeri casuali e li salva in un file;
#2) Se l'utente avrà indovinato 2 numeri avrà vinto, 
# altrimenti potrà arrendersi o ritentare per altri 3 tentativi


import random

numeri_casuali = random.sample(range(1, 20), 5)

print(numeri_casuali)

numeri_casuali2 = []
for i in numeri_casuali:
    numeri_casuali2.append(str(i))
    
print(numeri_casuali2)
    

with open("numeri.csv","w") as file:
    file.write(','.join(numeri_casuali2))