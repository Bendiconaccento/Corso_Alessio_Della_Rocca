

def decoratore(funzione):
    def wrapper(n):

        if funzione(n):
            print(f"{n} è un numero primo")
            return True
        
        else:
            print(f"{n} non è un numero primo")
            return False
    
    return wrapper


@decoratore

# Si determina se il numero è primo o no
def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):   # (n ** 0.5) è la radice quadrata. (+ 1) per includerre il limite superiore
        if n % i == 0:
            return False                  # Fa capire al decoratore che il numero non è primo
    return True                           # numero primo


def divisore(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i


def main():
    
    n_primi = []

    while True:

        nome = input("Inserisci il tuo nome o digita exit per uscire dal programma: ")

        if nome.lower() == "exit":
            break

        n = int(input("Inserisci un numero: "))

        if primo(n):
            n_primi.append(n)

        else:
            divis = divisore(n)
            print(f"Il divisore più piccolo di {n} è {divis}")

main()