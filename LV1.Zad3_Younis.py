lista_brojeva = []

while True:
    unos = input("Unesi brojeve (napisi Done za kraj)")

    if unos == "Done": 
        break

    try:
        broj = float(unos)
        lista_brojeva.append(broj)
    except ValueError:
        pass
        
uneseni_brojevi = len(lista_brojeva)
najmanji = min(lista_brojeva)
najveci = max(lista_brojeva)
prosjek = sum(lista_brojeva)
    
print("Unjeli ste ", uneseni_brojevi, "brojeva")
print("Najmanji broj je ", najmanji)
print("Najveci broj je ", najveci)
print("Prosjek brojeva je ", prosjek)