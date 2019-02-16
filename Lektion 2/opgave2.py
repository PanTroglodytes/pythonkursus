"""Dette program udskriver en liste af forfattere på hver deres linje, tilføjer én, fjerner én og udskriver"""

#Dette er listen over forfattere
yndlingsforfattere = ["Poulsen","Hansen","Jensen","Andersen","Møller"]

#her printer vi dem med et for-loop
for forfatter in yndlingsforfattere:
    print(forfatter)

#vi tilføjer en forfatter og udskriver igen
yndlingsforfattere.append("Strøm")

#her printer vi dem med et for-loop
for forfatter in yndlingsforfattere:
    print(forfatter)

#så sletter vi forfatter nummer 2
yndlingsforfattere.remove(yndlingsforfattere[1])

#her printer vi dem med et for-loop
for forfatter in yndlingsforfattere:
    print(forfatter)

