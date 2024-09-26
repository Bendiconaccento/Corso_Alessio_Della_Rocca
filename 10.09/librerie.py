

import math as m

#Il codice avrà le funzioni di math
#Che ho scritto con l'alias "m"

print(m.sqrt(30))

#per importare solo la funzione sqrt
from math import sqrt as s

print(s(30))


from math import sqrt, pow

print(pow(30))


from libreria_da_importare import somma


import random

#numero casuale tra 0 e 1
print(random.random())

print(random.randint(5, 100))

print(random.randrange(1, 100, 5))

lista = ["tommaso", "mirko","Alessio"]

print(random.choice(lista))


