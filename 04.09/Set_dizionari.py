
# # i valori non sono indicizzati, in ordine
# # in set non posso aggiungere valori se già contenuti 

# lista = [1,2,3,4,3,4]

# set_1 = {3,4,5}

# set_1.add(5)

# #mi toglie i doppioni
# print(set(lista))


# #dizionario #nome e cognome sono chiavi

# cliente1 = {1:{"nome": "tommaso","cognome" : "muraca"}}

# print(cliente1[1])

# cliente1["via"] = "via Giovanni"

# print(cliente1)

# for element in cliente1.values():
#     print(f"valore {element}")

# #valore temporaneo clienti.get
# #clienti.setdefault 

# #mi dice gli indici (posizione) dei valori della lista 
# lista2 = ["ciao","a","tutti"]
# print(list(enumerate(lista2)))



dizionario = {"nome": "Mario", "età": 30}

# Recuperiamo il valore della chiave "nome"
nome = dizionario.get("nome")
print(nome)  # Output: Mario


###### CON GET

dizionario = {"nome": "Mario", "età": 30}

# La chiave "indirizzo" non esiste, quindi restituisce il valore predefinito "Non disponibile"
indirizzo = dizionario.get("indirizzo", "Non disponibile")
print(indirizzo)  # Output: Non disponibile

##### SENZA GET
dizionario = {"nome": "Mario", "età": 30}

# Devi verificare manualmente se la chiave esiste per evitare errori
if "indirizzo" in dizionario:
    indirizzo = dizionario["indirizzo"]
else:
    indirizzo = "Non disponibile"

print(indirizzo)  # Output: Non disponibile



dizionario = {"nome": "Mario", "età": 30}

# La chiave "indirizzo" non esiste, quindi restituisce None
indirizzo = dizionario.get("indirizzo")
print(indirizzo)  # Output: None
