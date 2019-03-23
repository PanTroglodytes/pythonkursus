#Opbygning af ordbog
print("*** Velkommen til din Engelsk / Dansk-ordbog! Skriv et ord for at slå det op, eller skriv q for at forlade ordbogen ***")

opslag_igang = True
dansk_engelsk_ordbog = {"kat":"cat","bjørn":"bear","hund":"dog","bære":"bear"}
engelsk_dansk_ordbog = {}

for dansk_ord, engelsk_ord in dansk_engelsk_ordbog.items():
    if engelsk_ord not in engelsk_dansk_ordbog:
        engelsk_dansk_ordbog[engelsk_ord] = dansk_ord
    else:
        synonymliste = []
        synonymliste.append(engelsk_dansk_ordbog[engelsk_ord])
        synonymliste.append(dansk_ord)
        engelsk_dansk_ordbog[engelsk_ord] = synonymliste

while opslag_igang:
    opslag = input("Skriv et engelsk ord for at få det på dansk: ")
    if opslag == "q":
        opslag_igang = False
    else:
        if opslag in engelsk_dansk_ordbog:
            print(engelsk_dansk_ordbog[opslag])
        else:
            tilfoje = input("Ordet står ikke i ordbogen! skriv ja for at tilføje det eller nej for at vende tilbage til søgning ")
            while tilfoje == "ja":
                oversat_ord = input("Hvad hedder " + opslag + " på dansk? ")
                dansk_engelsk_ordbog[oversat_ord] = opslag
                tilfoje = "nej"

