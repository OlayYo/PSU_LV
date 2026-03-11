ime_datoteke = input("Unesi ime datoteke: ")

try:
    f.open(ime_datoteke)
except FileNotFoundError:
    print("Greska (datoteka ne postoji)")
    exit()