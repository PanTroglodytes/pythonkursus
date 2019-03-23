import time

langliste = []


for item in range(1,1000):
    langliste.append(str(item))

#tjekker i 2 løb
outputliste = []
start = time.time()

for item in langliste:
    if "9" in item:
        outputliste.append(item)

for item in langliste:
    if "9" not in item:
        outputliste.append(item)
end = time.time()
print("2 søgninger tog: ")
print(end - start)

#tjekker i 1 løb
outputliste = []
start = time.time()
for item in langliste:
    if "9" in item or "9" not in item:
        outputliste.append(item)

end = time.time()
print("1 søgning tog: ")
print(end - start)

