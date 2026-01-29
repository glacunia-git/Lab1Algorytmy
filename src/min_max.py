plik = open("../data/dane-lab1.txt", "r")
linie = plik.readlines()
plik.close()

dane = []

for linia in linie:
    tekst = linia.strip()
    if tekst != "":
        dane.append(tekst)


minimum = dane[0]
maksimum = dane[0]

for tekst in dane:
    if len(tekst) < len(minimum):
        minimum = tekst
    if len(tekst) > len(maksimum):
        maksimum = tekst

print("Liczba znaków:\n")
print(f"{minimum}")
print(f"{maksimum}\n")


def suma_ascii(tekst):
    suma = 0
    for znak in tekst:
        suma += ord(znak)
    return suma

minimum = dane[0]
maksimum = dane[0]

for tekst in dane:
    if suma_ascii(tekst) < suma_ascii(minimum):
        minimum = tekst
    if suma_ascii(tekst) > suma_ascii(maksimum):
        maksimum = tekst

print("Suma ASCII:\n")
print(f"{minimum}")
print(f"{maksimum}\n")


minimum = dane[0]
maksimum = dane[0]

for tekst in dane:
    if tekst < minimum:
        minimum = tekst
    if tekst > maksimum:
        maksimum = tekst

print("Alfabetycznie:\n")
print(f"{minimum}")
print(f"{maksimum}\n")