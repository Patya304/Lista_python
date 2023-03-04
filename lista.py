# 1. Melyik a legkisebb szám a listában?
# Készíts függvényt legkisebb() néven,  amely visszatér egy számokat tartalmazó lista legkisebb számával.
# Figyelem! A feladat megoldása során nem használhatod a min függvényt!


def legkisebb(lista):
    smallest = lista[0]
    for num in lista:
        if num < smallest:
            smallest = num
    return smallest


# 2. Mennyi a lista számainak összege?
# Készíts függvényt osszeg() néven,  amely visszatér egy számokat tartalmazó lista számainak összegével.
# Figyelem! A feladat megoldása során nem használhatod a sum függvényt!


def osszeg(lista):
    amount = 0
    for num2 in lista:
        amount = amount + num2
    return amount


# 3. Mennyi a listában levő számok szorzata?
# Készíts függvényt szorzat() néven,  amely visszatér egy számokat tartalmazó lista számainak szorzatával.


def szorzat(lista):
    product = 1
    for num3 in lista:
        product = product * num3
    return product


# 4. Mennyi a páros számok száma a listában?
# Készíts függvényt parosok_szama() néven,  amely visszatér egy számokat tartalmazó lista páros számainak számával.


def parosok_szama(lista):
    num_of_pairs = 0
    for num4 in lista:
        if num4 % 2 == 0:
            num_of_pairs = num_of_pairs + 1
    return num_of_pairs