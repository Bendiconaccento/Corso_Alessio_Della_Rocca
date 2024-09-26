

try:
    print(10/0)
    print("codice eseguito")
except:
    print("codice alternativo")

print("vai avanti")


#se dinamico

a = 10
b = 0

try:
    print(a/b)
    print("codice eseguito")
except ZeroDivisionError as e:
    print(f"codice alternativo, errore: {e}")

print("vai avanti")


#se errore che non riguarda la Zerodivision error o type error, mi prende il terzo except

a = 10
b = "ciao"

try:
    print(a/b)
    print("codice eseguito")
except ZeroDivisionError as e:
    print(f"codice alternativo, errore: {e}")
except TypeError as a:
    print(f"codice alternativo, errore: {a}")
except:
    print("errore")

print("vai avanti")

