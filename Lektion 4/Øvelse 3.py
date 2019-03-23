inventarliste = ["Tandbørste", "Sovepose", "t-shirt", "sokker", "pung", "briller", "kat"]
pakkeliste = []
taskestoerrelse = input("Hvor stor er tasken? :")
taskestoerrelse = int(taskestoerrelse)


for ting in inventarliste:
    while len(pakkeliste) < taskestoerrelse:
        svar = input("Vil du pakke " + ting + "?" + " skriv \"Ja\" eller \"Nej\" eller skriv \"afslut\" for at lukke tasken: ")
        if svar.lower() == "ja":
            pakkeliste.append(ting)
        if svar.lower() == "afslut":
            break

if len(pakkeliste) >= taskestoerrelse:
    print("din taske er fuld!")
print("Din taske indeholder: ")
for ting in pakkeliste:
    print(ting)