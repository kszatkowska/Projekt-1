def fibo(n):
    lista = []
    a=0
    b=1
    for i in range(n):
        lista.append(a)
        c=a+b
        a=b
        b=c
    return lista
n = int(input("Podaj ilość argumentów: "))
lista = fibo(n)
print(lista)