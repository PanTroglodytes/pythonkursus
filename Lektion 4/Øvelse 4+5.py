#Opbygning af ordbog
print("*** Velkommen til din Dansk / Engelsk-ordbog! Skriv et ord for at slå det op, eller skriv q for at forlade ordbogen ***")

opslag_igang = True
dansk_engelsk_ordbog = {"kat":"cat","bjørn":"bear","hund":"dog"}
while opslag_igang:
    opslag = input("Skriv et dansk ord for at få det på engelsk: ")
    if opslag == "q":
        opslag_igang = False
    else:
        if opslag in dansk_engelsk_ordbog:
            print(dansk_engelsk_ordbog[opslag])
        else:
            tilfoje = input("Ordet står ikke i ordbogen! skriv ja for at tilføje det eller nej for at vende tilbage til søgning ")
            while tilfoje == "ja":
                oversat_ord = input("Hvad hedder " + opslag + " på engelsk? ")
                dansk_engelsk_ordbog[opslag] = oversat_ord
                tilfoje = "nej"

