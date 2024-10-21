"""1. Feladat: Ajándékcsomagoló szalag számítás
Készítsünk programot, amely ajándékok csomagolásához szükséges szalag hosszát számolja ki.
A szalag hosszának úgy kell elegendőnek lennie, hogy kétszer körbeérje az ajándék körvonalát (téglalap alapú csomag esetén), és a masni készítéséhez további 50 cm szükséges.
A program kérje be az ajándék hosszát, szélességét és magasságát (cm-ben), az ajándékok számát, valamint a rendelkezésre álló szalag hosszát (méterben).
Számítsa ki, hogy hány méter szalagra van szükség a megadott számú ajándék csomagolásához, és közölje a felhasználóval, hogy elegendő-e a szalag.
"""

hossz = float(input("Add meg a csomag hosszát! "))
szeklet = float(input("Add meg a csomag szélességét! "))
magassag = float(input("Add meg a csomag magasságát! "))
szalaghossz = float(input("Add meg a szalag hosszát! "))
ajandek_szam = int(input("Mennyi ajándékot szeretnél? "))

kerulet1 = (szeklet + magassag) * 2
kerulet2 = (hossz + magassag) * 2

szalag_egy_ajandekra = kerulet1 + kerulet2 + 50

szukseges_szalag_cmben = szalag_egy_ajandekra * ajandek_szam
szukseges_szalag_meterben = szukseges_szalag_cmben / 100

print(f"A csomagolashoz szuksegse szalag: {szukseges_szalag_meterben} meter")

if szalaghossz > szukseges_szalag_meterben:
    print("ugyes kis cigany vagy")
else:
    print(f"buta geci vagy, kell meg {szukseges_szalag_meterben - szalaghossz}")
