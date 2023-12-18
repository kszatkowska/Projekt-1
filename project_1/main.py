import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime
import csv


def ex_1():
    print('Zadanie 1')
    for a in range(1, 101):
        if (a % 3 == 0) and (a % 5 == 0):
            print("FizzBuzz")
        elif a % 5 == 0:
            print("Buzz")
        elif a % 3 == 0:
            print('Fizz')
        else:
            print(a)
    pass

def ex_2():
    print('Zadanie 2')
    def losowe_liczby_plik(nazwa_pliku, ilosc_liczb):
        with open(nazwa_pliku, 'w') as plik:  # tworzenie pliku do zapisu losowych liczb
            for _ in range(ilosc_liczb):
                losowa_liczba = str(random.randint(1, 100))  # generowanie losowej liczby
                plik.write(losowa_liczba + '\n')  # przechodzenie do kolejnej linii

    nazwa_pliku = "losowe_liczby.txt"
    ilosc_liczb = int(input("Podaj liczbę losowych liczb, które chcesz zapisać: "))

    losowe_liczby_plik(nazwa_pliku, ilosc_liczb)
    pass

def ex_3():
    print('Zadanie 3')
    def losowe_liczby_plik(nazwa_pliku, ilosc_liczb):
        lista = []
        with open(nazwa_pliku, 'w') as plik:
            for _ in range(ilosc_liczb):
                losowa_liczba = (random.randint(1, 100))
                plik.write(str(losowa_liczba) + '\n')
                lista.append(losowa_liczba)
            return lista

    try:
        ilosc_liczb = int(input("Podaj liczbę losowych liczb do zapisania: "))
        lista = losowe_liczby_plik("zad3.txt", ilosc_liczb)
        print("Wygenerowane liczby to:", lista)
    except ValueError:
        print("bład")

    n = len(lista)
    srednia = sum(lista) / n
    print("Średnia wartość liczbowa to:", round(srednia, 2))
    pass

def ex_4(n):
    print('Zadanie 4')
    def fibo(n):
        lista = []
        a = 0
        b = 1
        for i in range(n):
            lista.append(a)
            c = a + b
            a = b
            b = c
        return lista

    n = int(input("Podaj ilość argumentów: "))
    lista = fibo(n)
    print(lista)
    return n

def ex_5():
    print('Zadanie 5')
    def fibo(n):
        lista = []
        a = 0
        b = 1
        for i in range(n):
            lista.append(a)
            c = a + b
            a = b
            b = c
        return lista

    def fibo_wykres(n):
        fibo_lista = fibo(n)
        plt.plot(range(n), fibo_lista, marker='o', linestyle='-', color='r')
        plt.title(f"Ciąg Fibonacciego dla n= {n}")
        plt.xlabel("Argument n")
        plt.ylabel("Wartości ciągu Fibonacciego")
        plt.grid(True)
        plt.show()

    try:
        n = int(input("Podaj ilość argumentów n: "))
        if n <= 0:
            print("Proszę podać liczbę naturalną większą od zera.")
        else:
            fibo_wykres(n)
    except ValueError:
        print("Podano nieprawidłową wartość. Proszę podać liczbę całkowitą.")

    pass

def ex_6():
    print('Zadanie 6')
    def new_dictionary(n):
        dictionary = {}

        for x in range(1, n):
            dictionary[x] = x ** 2

        return dictionary

    n = int(input("Podaj wartość n:"))

    created_dictionary = new_dictionary(n)
    print("Wygenerowano słownik:")
    print(created_dictionary)

    pass

def ex_7():
    print('Zadanie 7')
    def new_dictionary(n):
        dictionary = {}

        for x in range(1, n):
            dictionary[x] = x ** 2

        return dictionary

    n = int(input("Podaj wartość n:"))

    created_dictionary = new_dictionary(n)
    print("Wygenerowano słownik:")
    print(created_dictionary)

    sum_of_values = sum(created_dictionary.values())
    print("Suma wszystkich wygenerowanych wartości słownika wynosi:", sum_of_values)
    pass

def ex_8():
    print('Zadanie 8')
    import random
    from datetime import datetime
    def tworzenie_plików():
        ilosc_danych_do_zapisu = int(input("Podaj ilość danych do zapisu w plikach:"))
        aktualny_czas = datetime.now()
        for i in range(1, 11):
            nazwa_pliku = aktualny_czas.strftime("%Y_%m_%d_%H_%M_%S_%f") + f"_{i}.bin"
            try:
                with open(nazwa_pliku, 'wb') as plik:
                    liczby = bytearray([random.randint(0, 255) for _ in range(ilosc_danych_do_zapisu)])
                    plik.write(liczby)
                print(f"Zapisano {ilosc_danych_do_zapisu} losowych liczb do pliku binarnego {nazwa_pliku}")
            except Exception as e:
                print(f"Wystąpił błąd podczas zapisywania danych do pliku {nazwa_pliku}: {e}")

    tworzenie_plików()
    pass

def ex_9():
    print('Zadanie 9')

    def wczytaj_dane(plik_csv):
        timestamp, pos_x, pos_y, pos_z = [], [], [], []
        with open(plik_csv, 'r', newline='') as plik_csv:
            czytnik = csv.reader(plik_csv)
            next(czytnik)
            for wiersz in czytnik:
                timestamp.append(wiersz[0])
                pos_x.append(float(wiersz[1]))
                pos_y.append(float(wiersz[2]))
                pos_z.append(float(wiersz[3]))
        return timestamp, pos_x, pos_y, pos_z

    plik_csv = 'reference_trajectory.csv'
    timestamp, pos_x, pos_y, pos_z = wczytaj_dane(plik_csv)

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    # Wykres 1 x
    ax1.plot(timestamp, pos_x, color='red', label='pos_x')
    ax1.set_ylabel('pos_x')
    ax1.legend()

    # Wykres 2 y
    ax2.plot(timestamp, pos_y, color='blue', label='pos_y')
    ax2.set_ylabel('pos_y')
    ax2.legend()

    # Wykres 3 z
    ax3.plot(timestamp, pos_z, color='green', label='pos_z')
    ax3.set_ylabel('pos_z')
    ax3.set_xlabel('Timestamp')
    ax3.legend()

    plt.tight_layout()
    plt.show()

    pos_x_array = np.array(pos_x)
    pos_y_array = np.array(pos_y)
    pos_z_array = np.array(pos_z)

    s_pos_x = np.mean(pos_x_array)
    s_pos_y = np.mean(pos_y_array)
    s_pos_z = np.mean(pos_z_array)

    print(f"Średnia pozycja pos_x: {s_pos_x}")
    print(f"Średnia pozycja pos_y: {s_pos_y}")
    print(f"Średnia pozycja pos_z: {s_pos_z}")

    def oblicz_predkosc(pozycje):
        predkosc = [0]
        for i in range(1, len(pozycje)):
            delta_pozycji = pozycje[i] - pozycje[i - 1]
            delta_czasu = 1
            predkosc_punktu = delta_pozycji / delta_czasu
            predkosc.append(predkosc_punktu)
        return predkosc

    predkosc_x = oblicz_predkosc(pos_x)
    predkosc_y = oblicz_predkosc(pos_y)
    predkosc_z = oblicz_predkosc(pos_z)

    with open('velocity.csv', 'w', newline='') as plik_csv:
        writer = csv.writer(plik_csv)
        for vel_x, vel_y, vel_z in zip(predkosc_x, predkosc_y, predkosc_z):
            writer.writerow([vel_x, vel_y, vel_z])

    print("Dane prędkości zostały zapisane do pliku velocity.csv")
    pass


def main():
    ex_1()
    ex_2()
    ex_3()
    ex_5()
    ex_6()
    ex_7()
    ex_8()
    ex_9()

if __name__ == '__main__':
    main()