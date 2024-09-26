s= "Python"
print(s[0])
print(s[2])

a= "Ciao"
b= "Alice"
c= a + " " + b #se voglio lo spazio ci devo mettere le virgolette
print(c)

s= "Ciao Mondo, Mirko!"
print(len(s))
print(s.upper())
print(s.split(",")) #mette la virgola ad ogni parola
print(s.replace("Mondo","Universo"))

# al posto della visgola ci saranno i trattini
lista = ["ciao","a","tutti"]
separatore = "-"

stringa = separatore.join(list)
print(stringa)