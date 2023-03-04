'''
A lista.py fájlban kell dolgoznod!
Kérlek ne változtass ezen a fájlon
'''

from lista import legkisebb, osszeg, szorzat, parosok_szama

len = None
sum = None
min = None
max = None
l = [-90, 700, -600, 7000, -8001]
print(f'''
Ha a lista: {l}

Minta:
1. A listában levő legkisebb szám:     -8001
2. A listában levő számok összege:     -991
3. A listában levő számok szorzata:    -2117064600000000
4. A listában levő páros számok száma:  4
-----------------------------------------------------
A program futásának eredménye:
1. A listában levő legkisebb szám:     {legkisebb(l)}
2. A listában levő számok összege:     {osszeg(l)}
3. A listában levő számok szorzata:    {szorzat(l)}
4. A listában levő páros számok száma:  {parosok_szama(l)}
      
Figyelem! 
Minden feladat után futtasd le a unit teszteket!
A dolgozat beadásához nyomd meg a submit gombot.
''')