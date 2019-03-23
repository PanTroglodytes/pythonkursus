import klasser as k

bog1 = k.Bog(12345680,"Python Crash Course",1,0,2016,525,"Eric Matthes")
materiale2 = k.Materiale(12345679,"Absolute Jacoby",2,1,2020)
film1 = k.Film(12345681,"Alien",15,2,1978,"Ridley Scott",124)

print(bog1.kan_udlaanes())
print(bog1.udlaan())
print(bog1.kan_udlaanes())
print(bog1.udlaan())

print(bog1.match_titel("Python"))
print(film1.match_titel("Python"))
print(bog1.match_titel("li"))
print(film1.match_titel("li"))