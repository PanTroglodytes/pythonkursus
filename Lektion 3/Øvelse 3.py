#Laver for-loops i dictionaries

navne = {"Emil" : "Hansen", "Søren" : "Staugaard", "Egon" : "Rose", "Giorgos" : "Rastapopoulos", "Steinbjørn" : "Ulfsbane"}

for fornavn in navne:
    print(fornavn)

for efternavn in navne.values():
    print(efternavn)

for fornavn, efternavn in navne.items():
    print(fornavn+" "+efternavn)


