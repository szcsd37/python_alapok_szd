"""2. Feladat
Írj egy programot, amely csökkenő sorrendben írja ki a számokat 1 és 10 között!"""

x = 10
while x >= 1:
    print(x)
    x -= 1


"""3. Feladat
Írj egy programot, amely kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között!
"""
print("\n\033[1m3. feladat\033[0m\n")

y = 10
while y >= 1:
    if y % 2 != 0:
        print(y)
    y -= 1