
def is_prime(n):

#Funzione che determina se un numero è primo. (Chat)

    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Il programma dovrebbe controllare se il numero inserito è primo o no.
# Se è primo, lo salva e stampa "Il numero è primo".
# Altrimenti, stampa "Il numero non è primo". si ferma iltutto quando ha 5 numeri primi
 
# Lista per memorizzare i numeri primi trovati
numeri_primi = []

# il ciclo contiua a chiedere numeri all'utente fino a che non ce ne sono 5 in lista
while len(numeri_primi) < 5:
    numero = int(input("Inserisci un numero: "))
    
    # Verifica che l'input sia costituito solo da cifre
    #if numero.isdigit():
    #    numero = int(numero)
        
    # Verifica se il numero è primo
    if numero > 1:
        primo = True

        #Controlla se il numero è divisibile per qualche numero tra 2 e la radice quadrata del numero stesso. Se lo è, il numero non è primo.
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                primo = False
                break
            
        if primo:
            # aggiungi alla lista
            numeri_primi.append(numero)
            print(f"Il numero {numero} è primo.")
        
        else:
            print(f"Il numero {numero} non è primo.")
    
    else:
        print(f"Il numero {numero} non è primo.")

else:
    print("Hai inserito un numero non valido.")
    
# Stampa la lista dei numeri primi trovati
print(f"Hai inserito 5 numeri primi: {numeri_primi}")
