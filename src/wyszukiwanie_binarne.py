from sortowania import sortowanie_scalanie

plik = open("../data/liczby-sortowanie.txt")
dane = plik.read().split()
plik.close()

liczby = []
for x in dane:
    liczby.append(int(x))


posortowane = sortowanie_scalanie(liczby)


def wyszukiwanie_binarne(lista, x):
    lewy = 0
    prawy = len(lista) - 1

    while lewy <= prawy:
        srodek = (lewy + prawy) // 2

        if lista[srodek] == x:
            return srodek
        elif lista[srodek] < x:
            lewy = srodek + 1
        else:
            prawy = srodek - 1

    return -1


szukana = int(input("Podaj liczbę do wyszukania: "))

wynik = wyszukiwanie_binarne(posortowane, szukana)

if wynik != -1:
    print("Znaleziono", szukana, "na indeksie", wynik)
else:
    print("Nie znaleziono", szukana)