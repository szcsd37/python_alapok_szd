#
"""Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót."""


# x = int(input("Adj meg egy egész számot! "))

#if x % 2 == 0 and x > 0:
 #   print("A szám páros és pozitív.")
#elif x % 2 != 0 and x < 0:
#    print("A szám negatív és páratlan.")
#else:
#    print("A szám egyik feltételnek sem felel meg.")

#
"""Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi, hogy az ikrek (Henrik és Hanna) jönnek-e ma kosrazni! Például így: Jön Henrik ma kosarazni? (igen/nem). A program írja ki, hogy melyik állítás igaz az alábbiak közül:
- egyikük sem jön kosarazni,
- mind a ketten jönnek kosarazni,
- csak az egyikük jön kosarazni.
"""

hanna = input("Hanna jön ma kosarazni?(igen/nem) ")
henrik = input("Henrik jön ma kosarazni?(igen/nem) ")

if henrik == "nem" and hanna == "igen":
    print("egyikük jön kosarazni.")
if henrik == "igen" and hanna == "nem":
    print("egyikük jön kosarazni.")
elif henrik and hanna == "igen":
    print("Mind a ketten jönnek kosarazni.")
elif henrik and hanna == "nem":
    print('Nem jönnek kosarazni.')

