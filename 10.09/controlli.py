

inputUtente = "18"

# if inputUtente.isdecimal():
#     print("è un numero")
#     print(int(inputUtente))

# else:
#     print("non è un numero")

try:
    print(int(inputUtente))

except:
    print("Valore non valido")

print("Fuori costrutto")




def divisione(a,b):
    return a/b
a=10
b=0

try:
    print(divisione(a,b))

except:
    print("Valore non valido")

print("Fuori costrutto")


def divisione(a,b):
    return a/b
a=10
b=0

try:
    print(divisione(a,b))

except ZeroDivisionError as e:
    print(f"Valore non valido, errore{e}")

print("Fuori costrutto")

