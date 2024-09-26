

import pickle

"""""
dizionario = {1: "tommaso", 2:"mirko"}

dizB = pickle.dumps(dizionario)

with open("binario.bin", "wb") as myfile:
    myfile.write(dizB)"""""


with open("binario.bin", "wb") as myfile:
    contenuto = myfile.read()

contenuto = pickle.loads(contenuto)
print(contenuto)