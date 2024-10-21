"""2. Feladat: Festék mennyiségének számítása
Készítsünk programot, amely egy szoba falainak kifestéséhez szükséges festék mennyiségét számolja ki.
A program kérje be a szoba szélességét, hosszát és magasságát méterben, valamint azt, hogy hány liter festéket vásároltunk már.
Tegyük fel, hogy 1 liter festék 10 négyzetmétert fed le.
Számolja ki, hogy hány liter festékre van szükség a szoba kifestéséhez, és közölje, hogy elegendő-e a festék, vagy szükség van-e további mennyiség beszerzésére.
"""
szelesseg = int(input("Adja meg a szoba szelesseget! "))
magassag = int(input("Add meg a fal magasságát! "))
hossz = int(input("Add meg a fal hosszát! "))
megvett_festek = int(input("Mennyi festéket vettél meg? "))


fal1 = 2 * (szelesseg * magassag)
fal2 = 2 * (hossz * magassag)
kello_festek = (fal1 + fal2) / 10
kell_meg = kello_festek - megvett_festek


if kello_festek > megvett_festek:
   print(f"nem eleg a festek, kell meg {kell_meg}")
else:
   print("eleg")
