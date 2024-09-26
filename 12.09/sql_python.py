import mysql.connector


mydb = mysql.connector.connect(
    #server fisico
    host = "localhost",
    #dati accesso host
    user = "root",
    password = "root",
    port = 8889,
    database = "esercitazionepython"
)

print(mydb)


## creare un cursore che fa qualcosa sul database (interagire su db)
#mycursor = mydb.cursor()

#creare una query
#sql = "create database esercitazionepython"

#eseguire la query
#mycursor.execute(sql)

# visualizzare db
#sql = "show databases"

#mycursor.execute(sql)

#for db in mycursor:
#    print(f"database: {db}")

#creare una tabella
#sql = "create table utenti(id int auto_increment primary key, nome varchar(255), cognome varchar(255))"

mycursor = mydb.cursor()

def inserisciDati():


#sql = "show table"
#mycursor.execute(sql)

#for tb in mycursor:
    #print(f"Tabella: {tb}")

#inserire dati nel db
#creo query       %s = segnaposto, permette di lavorare con dati dinamici. SQL injection, una persona inserisce una stringa senza fare danni.
    sql = "insert into utenti(nome, cognome) values(%s,%s)"

#tupla di valori  PER FARE LA TUPLA DOPO IL SECONDO PARAMETRO POTREBBE VOLERCI LA VIRGOLA
    val = ("tommaso","muraca")
    mycursor.execute(sql, val)

#da l'autorizzazione a inserire i dati nella tabella
#mydb.commit()

#print(mycursor.rowcount,"record inseriti")

#lista di tuple si deve mettere executeMANY
#val = [("tommaso","muraca"),("marco","rossi"),("fra","verdi")]
#mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount,"record inseriti")

#stampa l'ID dell'ultima riga caricata
    print(mycursor.lastrowid)

def selezione():
#query 
    sql = "select * from utenti where id>3"

    mycursor.execute(sql)

#prendi tutti i dati presenti nel cursore
#.fetchone() se voglio solo il primo elemento
    dati = mycursor.fetchall()

    for dato in dati:
        print(dato)

#per eliminare 
def delete():

    sql = "delete from utenti where id>4"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "righe eliminate")

delete()

#eliminare tabella intera
'''
mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)'''

#modificare la struttura del db
'''
mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")'''