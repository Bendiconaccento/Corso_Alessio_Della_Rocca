livello_1 = input("Inserire codice di primo livello: ") 

if livello_1 == "0001":                   #per poter proseguire è necessario spostarsi avanti di livello 
    print("Livello 1 superato")

    livello_2 = input("inserisci codice di secondo livello: ")

    if livello_2 == "0002":
     print("Livello 2 superato")

     livello_3= input("Inserire codice terzo livello: ")

     if livello_3 == "0003":
        print("Codice corretto")

     else:
       print("codice 3 errato")
   
    else:
       print("codice 2 errato")
else:
   print("Codice 1 errato")

     