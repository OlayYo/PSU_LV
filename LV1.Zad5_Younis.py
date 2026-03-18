try:
    fhand = open("song.txt")
except:
    print("Greška: datoteka song.txt nije pronađena.")
    quit()

rjecnik = {}

for linija in fhand:
    linija = linija.rstrip()
    rijeci = linija.split()

    for rijec in rijeci:
        rijec = rijec.lower()

        if rijec in rjecnik:
            rjecnik[rijec] = rjecnik[rijec] + 1
        else:
            rjecnik[rijec] = 1

fhand.close()

samo_jednom = []

for rijec in rjecnik:
    if rjecnik[rijec] == 1:
        samo_jednom.append(rijec)

print("Ukupno različitih riječi:", len(rjecnik))
print()
print("Broj riječi koje se pojavljuju samo jednom:", len(samo_jednom))
print("To su:")
for r in samo_jednom:
    print(" ", r)
