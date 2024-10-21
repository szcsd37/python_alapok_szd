"""1. Páros és páratlan számok szétválogatása (1-től 20-ig)
Feladat: Írd ki külön a páros és a páratlan számokat 1-től 20-ig."""
def elso_feladat():
    parosak = []
    paratlanok = []

    for i in range(1, 21):
        if i % 2 == 0:
            parosak.append(i)
        else:
            paratlanok.append(i)

    print(f"paros szamok:{parosak}")
    print(f"paratlan szamok:{paratlanok}")






"""2. Számok faktoriálisa
Feladat: Számold ki egy adott szám faktoriálisát!"""
def masodik_feladat():

    szam = 7
    faktorialis = 1

    for i in range(1, szam +1):
        faktorialis *= i

    print(faktorialis)



"""3. Számok összegének és átlagának kiszámolása
Feladat: Számold ki az 1-től egy adott számig lévő számok összegét és átlagát!

Ha az adott szám 10:
Összeg: 1 + 2 + 3 + ... + 10 = 55
Átlag: 55 ÷ 10 = 5.5
"""
def harmadik_feladat():
    n_szam = 10
    osszeg = 0

    for i in range(1, n_szam +1):
        osszeg = osszeg + i
    atlag = osszeg / n_szam
    print(f"{n_szam} szám átlaga: {atlag}")




"""4. Egymásba ágyazott for ciklusok: szorzótábla megjelenítése
Feladat: Készítsd el az 1-től 10-ig tartó szorzótáblát!

Szorzótábla 1-től 10-ig:
1 × 1 = 1, 1 × 2 = 2, ..., 1 × 10 = 10
2 × 1 = 2, 2 × 2 = 4, ..., 2 × 10 = 20
...
10 × 1 = 10, 10 × 2 = 20, ..., 10 × 10 = 100
"""
def negyedik_feladat():
    # szam1 = 1
    # for i in range(1, 11):
    #     print(f"{szam1} x {i} = {szam1 * i}")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}",end=" ")
            print()


"""5. Fibonacci-sorozat generálása
Feladat: Írd ki a Fibonacci-sorozat első 10 számát!

Fibonacci-sorozat első 10 száma: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34"""






# elso_feladat()
# masodik_feladat()
# harmadik_feladat()
# negyedik_feladat()
