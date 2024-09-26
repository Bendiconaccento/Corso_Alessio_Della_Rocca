# Credenziali predefinite
nome = "Alessio"
chiave = "oisselA"

# Primo tentativo di accesso
username = input("Nome utente: ")
password = input("Password: ")

if username == nome and password == chiave:
    print("Accesso consentito")
else:

    # Nome utente corretto ma password sbagliata
    if username == nome:
        print("Password errata. Reimposta la password.")
        chiave = input("Nuova password: ")                   # Aggiorna la variabile chiave

        if chiave == password:                               # La nuova nuova deve essere uguale a quella vecchia
            print("Accesso consentito con nuova password.")
        else:
            print("Password errata. Accesso negato.")
    
    # Password corretta ma nome utente sbagliato
    elif password == chiave:
     print("Nome utente errato. Reimposta il nome utente.")
     nome = input("Nuovo nome utente: ")                      # Aggiorna la variabile nome
     
     if nome == username:
      print("Accesso consentito con nuovo nome utente.")
     else:
      print("Nome utente errato. Accesso negato.")
    
    # Nome utente e password sbagliati
    else:
     print("User name e password errati, reimposta entrambe.")
     nome = input("Nuovo nome utente: ")                       # Aggiorna la variabile nome
     chiave = input("Nuova password: ")                        # Aggiorna la variabile chiave
    
     if chiave == password and nome == username:
      print("Accesso consentito con nuovo nome utente e password.")
     else:
      print("Accesso negato.")

# Scelta della domanda di sicurezza
if chiave == password and nome == username:
 scelta = int(input("Seleziona il numero corrispondente di una domanda segreta: 1) Colore preferito 2) Animale preferito: "))

 if scelta == 1:
    op_1 = input("Inserisci il colore preferito: ")
    print("Il colore preferito è stato aggiunto")
    print("Accesso consentito")

 elif scelta == 2:
    op_2 = input("Iserisci l'animale preferito: ")
    print("L'animale preferito è stato aggiunto")
    print("Accesso consentito")

else:
  print("Numero non valido, accesso negato")


