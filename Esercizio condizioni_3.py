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

        if chiave == password:                               # La nuova 
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





