# inizializzazione lista numeri
numeri=[]

while True:
 # Se usassi int() direttamente su input(), il codice darebbe un errore quando l'utente inserisce "s", 
 # perché non è possibile convertire "s" in un intero
 n = input("Inserisci un numero o premi s per interrompere: ")
 if n == "s":
  break
 
 # inserisco i numeri inseriti dall'utente (n) nella lista vuota (numeri).
 # Solo dopo aver verificato che l'utente non vuole interrompere, 
 # il programma tenta di convertire n in un intero con int(n)
 numeri.append(int(n)**2)
 print(numeri)