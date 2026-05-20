fhand = open("SMSSpamCollection.txt")

ham_rijeci = 0
ham_poruka = 0
spam_rijeci = 0
spam_poruka = 0
spam_usklik = 0

for linija in fhand:
    linija = linija.rstrip()
    dijelovi = linija.split("\t")

    tip = dijelovi[0]
    poruka = dijelovi[1]
    rijeci = poruka.split()

    if tip == "ham":
        ham_rijeci = ham_rijeci + len(rijeci)
        ham_poruka = ham_poruka + 1
    elif tip == "spam":
        spam_rijeci = spam_rijeci + len(rijeci)
        spam_poruka = spam_poruka + 1
        if poruka.endswith("!"):
            spam_usklik = spam_usklik + 1

fhand.close()

print("a) Prosjecan broj rijeci u ham porukama:", ham_rijeci / ham_poruka)
print("   Prosjecan broj rijeci u spam porukama:", spam_rijeci / spam_poruka)
print()
print("b) Broj spam poruka koje zavrsavaju uskličnikom:", spam_usklik)
