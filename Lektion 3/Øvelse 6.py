lande = ["Tyskland", "Danmark", "Sverige", "Norge"]

#leder efter substreng "mark"
substreng = "mark"

for land in lande:
    print("leder efter " + substreng)
    print("tjekker "+land)
    if substreng in land:
        print("Yes, der var den")
        break
    else:
        print("Det var ikke i " + land)