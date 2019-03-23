import klasser as k

bog1 = k.Bog(12345680,"Python Crash Course",1,0,2016,525,"Eric Matthes")
materiale2 = k.Materiale(12345679,"Absolute Jacoby",2,1,2020)
film1 = k.Film(12345681,"Alien",15,2,1978,"Ridley Scott",124)

if isinstance(bog1, k.Bog):
   print("bog1 er en Bog")
else:
   print("bog1 er ikke en Bog")

if isinstance(film1,k.Film):
   print("film1 er en Film")
else:
   print("film1 er ikke en film")

if isinstance(film1,k.Materiale):
   print("film1 er Materiale")
else:
   print("film1 er ikke Materiale")

if isinstance(film1,k.Bog):
   print("film1 er en Bog")
else:
   print("film1 er ikke en Bog")
