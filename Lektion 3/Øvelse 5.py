#nesting i dictionaries

byer_de = {"Land" : "Tyskland", "Byer" : ["Berlin", "München", "Hamburg"]}
byer_gb = {"Land" : "Storbritannien", "Byer" : ["London", "Birmingham", "Manchester"]}
byer_fr = {"Land" : "Frankrig", "Byer" : ["Paris", "Marseille", "Lyon"]}

byer_i_lande = []
byer_i_lande.append(byer_de)
byer_i_lande.append(byer_gb)
byer_i_lande.append(byer_fr)

for byliste in byer_i_lande:
    print("\nLand: "+byliste["Land"])
    print("Byer: ")
    for by in byliste["Byer"]:
        print(by)