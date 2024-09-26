

#contesto, indirizzo di memoria, modo in cui voglio interagire con il file
with open("test.txt", "a") as myfile:
    myfile.write("primo file creato")

# mi crea un nuovo file in .txt
# se ci riclicco scrive attaccato a primo file creato un altro "primo file creato"
# se metto \n mette a capo "primo file creato"

#serve a scrivere un file
def funz_write():
    with open("test.txt", "w") as myfile:
    myfile.write("primo file creato")

#serve a leggere il file
def read_file():
    with open("test.txt", "r") as myfile:
        contenuto = myfile.readlines()
    return contenuto

print(read_file())

