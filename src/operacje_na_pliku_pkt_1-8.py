import os

dane_wejsciowe = "../data/wprowadzenie-dane.txt"
zapis_ponumerowane = "../results/wprowadzenie_ponumerowane.txt"
zapis_bez_bialych_znakow = "../results/wprowadzenie_bez_bialych_znakow.txt"

file = open(dane_wejsciowe, "r", encoding="utf-8")
lines = []
for line in file:
    lines.append(line)  # line zawiera też "\n" na końcu
file.close()

line_count = len(lines)
print("Liczba linii w pliku:", line_count)

ponumerowane_linijki = []
i = 1
for line in lines:
    ponumerowane_linijki.append(str(i) + ". " + line)
    i += 1

os.makedirs("results", exist_ok=True)

out = open(zapis_ponumerowane, "w", encoding="utf-8")
for line in ponumerowane_linijki:
    out.write(line)
out.close()

bez_bialych_znakow = []

for line in lines:
    tekst = line.rstrip("\n")
    ma_biale_znaki = False

    for ch in tekst:
        if ch.isspace():
            ma_biale_znaki = True
            break

    if not ma_biale_znaki:
        bez_bialych_znakow.append(line)

out = open(zapis_bez_bialych_znakow, "w", encoding="utf-8")
for line in bez_bialych_znakow:
    out.write(line)
out.close()

do_kwadratu = []

for line in lines:
    tekst = line.strip()

    if tekst.startswith("-"):
        liczba = tekst[1:]
    else:
        liczba = tekst

    if liczba.isdigit():
        x = int(tekst)
        do_kwadratu.append(x * x)


do_kwadratu.sort()
print("Posortowane kwadraty liczb:")
for num in do_kwadratu:
    print(num)