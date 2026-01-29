import time


plik = open("../data/liczby-sortowanie.txt")
dane = plik.read().split()
plik.close()

liczby = []

for x in dane:
    liczby.append(int(x))
if __name__ == "__main__":
    print("Ilość liczb:", len(liczby))



def sortowanie_babelkowe(lista):
    a = lista[:]

    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

    return a




def sortowanie_wybieranie(lista):
    a = lista[:]

    for i in range(len(a)):
        najmniejszy = i

        for j in range(i + 1, len(a)):
            if a[j] < a[najmniejszy]:
                najmniejszy = j

        temp = a[i]
        a[i] = a[najmniejszy]
        a[najmniejszy] = temp

    return a



def sortowanie_wstawianie(lista):
    a = lista[:]

    for i in range(1, len(a)):
        aktualna = a[i]
        j = i - 1

        while j >= 0 and a[j] > aktualna:
            a[j + 1] = a[j]
            j = j - 1

        a[j + 1] = aktualna

    return a


def sortowanie_scalanie(lista):
    if len(lista) <= 1:
        return lista

    srodek = len(lista) // 2
    lewa = sortowanie_scalanie(lista[:srodek])
    prawa = sortowanie_scalanie(lista[srodek:])

    wynik = []
    i = 0
    j = 0

    while i < len(lewa) and j < len(prawa):
        if lewa[i] < prawa[j]:
            wynik.append(lewa[i])
            i += 1
        else:
            wynik.append(prawa[j])
            j += 1

    while i < len(lewa):
        wynik.append(lewa[i])
        i += 1

    while j < len(prawa):
        wynik.append(prawa[j])
        j += 1

    return wynik


def sortowanie_zliczanie(lista):
    if len(lista) == 0:
        return lista

    najmniejsza = min(lista)
    najwieksza = max(lista)

    liczniki = []

    for i in range(najwieksza - najmniejsza + 1):
        liczniki.append(0)

    for x in lista:
        liczniki[x - najmniejsza] += 1

    wynik = []

    for i in range(len(liczniki)):
        for j in range(liczniki[i]):
            wynik.append(i + najmniejsza)

    return wynik

if __name__ == "__main__":

    start = time.time()
    t1 = sortowanie_babelkowe(liczby)
    print("Sortowanie bąbelkowe:", time.time() - start)

    start = time.time()
    t2 = sortowanie_wybieranie(liczby)
    print("Sortowanie przez wybieranie:", time.time() - start)

    start = time.time()
    t3 = sortowanie_wstawianie(liczby)
    print("Sortowanie przez wstawianie:", time.time() - start)

    start = time.time()
    t4 = sortowanie_scalanie(liczby)
    print("Sortowanie przez scalanie:", time.time() - start)

    start = time.time()
    t5 = sortowanie_zliczanie(liczby)
    print("Sortowanie przez zliczanie:", time.time() - start)
