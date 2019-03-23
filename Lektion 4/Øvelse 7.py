""" omskrivning af for-løkker til while-løkker
for x in range(0,11):
print(x)
"""

counter = 1
while counter < 11:
    print(counter)
    counter += 1


print("********************************************************")
""" omskrivning af while-løkke til for-løkke
tal = [20,30,40,50,60,70]
index = 0
while tal[index]<50:
   print(tal[index])
   index+=1
"""

tal = [20,30,40,50,60,70]
for tal in tal:
    if tal < 50:
        print(tal)

print("******************************************")

""" uendelig løkke med for-loop
while (True):
   print("uendelig løkke")
"""

