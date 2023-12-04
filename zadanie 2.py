import random

def losowe_liczby_plik(nazwa_pliku, ilosc_liczb):
    with open(nazwa_pliku, 'w') as plik:  #tworzenie pliku do zapisu losowych liczb
        for _ in range(ilosc_liczb):
            losowa_liczba = str(random.randint(1, 100)) #generowanie losowej liczby
            plik.write(losowa_liczba + '\n')   #przechodzenie do kolejnej linii

nazwa_pliku = "losowe_liczby.txt"
ilosc_liczb = int(input("Podaj liczbę losowych liczb, które chcesz zapisać: "))

losowe_liczby_plik(nazwa_pliku, ilosc_liczb)