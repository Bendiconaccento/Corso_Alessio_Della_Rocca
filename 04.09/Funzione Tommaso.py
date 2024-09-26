

# età = 20
patente = "si"
# usoDiAlcool = "si"

# if età < 18:
#     print("non puoi guidare perchè minorenne")
# elif patente != "si":
#     print("non puoi guidare perchè non hai la patente")
# elif usoDiAlcool == "si":
#     print("non puoi guidare perché hai bevuto")
# else:
#     print("puoi guidare")



guida = "non puoi guidare perchè non hai la patente" if patente != "si" else "puoi guidare"

print(guida)