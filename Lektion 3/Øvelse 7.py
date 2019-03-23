landeliste = ["Spanien", "Rumænien", "Ægypten", "Vietnam", "Italien", "Rhodesia"]
resultatliste = []
soegestreng = "ien"

for land in landeliste:
    print("søger i " + land)
    if soegestreng in land:
        resultatliste.append(land)

print(soegestreng + " er i følgende lande:")
print(resultatliste)