import random
def losowe_liczby_plik(nazwa_pliku, ilosc_liczb):
    lista = []
    with open(nazwa_pliku, 'w') as plik:
        for _ in range(ilosc_liczb):
            losowa_liczba = (random.randint(1, 100))
            plik.write(str(losowa_liczba) + '\n')
            lista.append(losowa_liczba)
        return lista
try:
    ilosc_liczb= int(input("Podaj liczbę losowych liczb do zapisania: "))
    lista = losowe_liczby_plik("zad3.txt", ilosc_liczb)
    print("Wygenerowane liczby to:",lista)
except ValueError:
    print("bład")

n= len(lista)
srednia= sum(lista)/n
print("Średnia wartość liczbowa to:", round(srednia, 2))

suma_k = 0
for liczba in lista:
    suma_k += (liczba - srednia) ** 2
odchylenie_std = (suma_k/ n) ** 0.5

print("Odchylenie standardowe:", round(odchylenie_std, 2))

minimum_wartosc = min(lista)
maks_wartosc = max(lista)

print("Minimalna wartość to:", minimum_wartosc)
print("Maksymalna wartość to:", maks_wartosc)