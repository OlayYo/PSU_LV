naziv = input("Ime datoteke: ")

try:
    fhand = open(naziv)
except:
    print("Greška: datoteka", naziv, "nije pronađena.")
    quit()

ukupno = 0.0
broj = 0

for linija in fhand:
    linija = linija.rstrip()

    if linija.startswith("X-DSPAM-Confidence:"):
        dijelovi = linija.split()
        vrijednost = float(dijelovi[1])
        ukupno = ukupno + vrijednost
        broj = broj + 1

fhand.close()

if broj > 0:
    prosjek = ukupno / broj
    print("Average X-DSPAM-Confidence:", prosjek)
else:
    print("Nisu pronađene X-DSPAM-Confidence linije u datoteci.")
