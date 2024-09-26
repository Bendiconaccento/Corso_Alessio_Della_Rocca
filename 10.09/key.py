
dizionario = {"a":1,"b":13,"c":11, "d":5}

lista_valori =list(dizionario.values())

lista_chiavi = list(dizionario.keys())

dizionario2 = dict(zip(lista_valori,lista_chiavi))

for element in sorted(dizionario2, reverse=True):
    print(f"chiave originaria: {dizionario2[element]}, valore originario: {element}")