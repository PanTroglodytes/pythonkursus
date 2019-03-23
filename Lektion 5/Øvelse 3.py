def add_sum_to_liste(liste):
    output_sum = 0
    for nummer in liste:
        output_sum+=nummer
    liste.append(output_sum)


liste =[1,2,3]

print(liste)
add_sum_to_liste(liste)
print(liste)

