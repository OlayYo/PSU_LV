#Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je plaćen po radnom satu. Koristite ugrađenu
#Python metodu input(). Nakon toga izračunajte koliko je korisnik zaradio i ispišite na ekran. Na kraju prepravite
#rješenje na način da ukupni iznos izračunavate u zasebnoj funkciji naziva total_euro.

def total_euro(sati, cijena_po_satu):
    return sati * cijena_po_satu

sati = float(input("Unesite broj radnih sati: "))
cijena_po_satu = float(input("Unesi koliko ste placeni. "))

zarada=total_euro(sati, cijena_po_satu)

print("Ukupna zarada je", zarada)