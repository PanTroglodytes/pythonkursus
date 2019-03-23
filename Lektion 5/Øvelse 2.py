def sum_af_lister(liste):
    output_sum = 0
    for nummer in liste:
        output_sum+=nummer
    return output_sum


liste =[1,2,3]

print(sum_af_lister(liste))