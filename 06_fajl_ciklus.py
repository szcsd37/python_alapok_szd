"""5. Feladat
Írj egy programot, amely a felhasználótól páros számot kér be. Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig, amíg végül páros számot nem ad meg a felhasználó.
"""



paros_szam = False

while paros_szam == False:
    felhasznaloi_input = int(input("Adj meg egy számot! "))
    if felhasznaloi_input % 2 == 0:
        paros_szam = True
        print("oke")

