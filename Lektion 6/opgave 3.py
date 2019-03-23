import klasser as k

bog1 = k.Bog(12345680,"Python Crash Course",1,0,2016,525,"Eric Matthes")
materiale2 = k.Materiale(12345679,"Absolute Jacoby",2,1,2020)
film1 = k.Film(12345681,"Alien",15,2,1978,"Ridley Scott",124)

materialeliste = [bog1,materiale2,film1]

for ting in materialeliste:
    print(ting.tostring())

