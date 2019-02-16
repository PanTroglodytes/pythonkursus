list_of_integers = []

while len(list_of_integers) < 100:
    list_of_integers.append(len(list_of_integers))

print(list_of_integers)

for thing in list_of_integers:
    print(thing**thing)