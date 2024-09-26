# per crea_numeri

def vuoi_proseguire():
    choice = input("vuoi proseguire? (y/n)")
    return choice
        
  
    
with open("numeri.csv","r") as file:
    lista = file.read()

lista_numerica = lista.split(',')

print(lista_numerica)

for i in range(3):
    numero1 = input("Inserisci numero 1 : ")
    numero2 = input("Inserisci numero 2 : ")
    
    if numero1 in lista_numerica and numero2 in lista_numerica:
        print("Hai indovinato")
        break
    elif numero1 in lista_numerica:
        print(f"Hai indovinato solo {numero1}")
        n = vuoi_proseguire()
        if n == 'n':
            break
    elif numero2 in lista_numerica:
        print(f"Hai indovinato solo {numero2}")
        n = vuoi_proseguire()
        if n == 'n':
            break
    else:
        n = vuoi_proseguire()
        if n == 'n':
            break
        print("Non hai indovinato")
    