"""1. Páros és páratlan számok szétválogatása (1-től 20-ig)
Feladat: Írd ki külön a páros és a páratlan számokat 1-től 20-ig."""
def elso_feladat:
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

faktori = int(input("Adj meg egy számot! "))

for i in range(1, faktori + 1):


"""3. Számok összegének és átlagának kiszámolása
Feladat: Számold ki az 1-től egy adott számig lévő számok összegét és átlagát!

Ha az adott szám 10:
Összeg: 1 + 2 + 3 + ... + 10 = 55
Átlag: 55 ÷ 10 = 5.5
"""

"""4. Egymásba ágyazott for ciklusok: szorzótábla megjelenítése
Feladat: Készítsd el az 1-től 10-ig tartó szorzótáblát!

Szorzótábla 1-től 10-ig:
1 × 1 = 1, 1 × 2 = 2, ..., 1 × 10 = 10
2 × 1 = 2, 2 × 2 = 4, ..., 2 × 10 = 20
...
10 × 1 = 10, 10 × 2 = 20, ..., 10 × 10 = 100
"""

"""5. Fibonacci-sorozat generálása
Feladat: Írd ki a Fibonacci-sorozat első 10 számát!

Fibonacci-sorozat első 10 száma: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34"""

# elso_feladat()