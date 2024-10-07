#import random

#random_szam = random.randint(1, 3)

#megadott_szam = int(input("Adj meg egy számot! "))


#if random_szam == megadott_szam:
#    print("A két szám egyenlő.")
#elif random_szam > megadott_szam:
#    print("A megadott szám kisebb.")
#elif random_szam < megadott_szam:
#    print("A megadott szám nagyobb.")


import random
penzerme = ("fej", "írás")
dobas = random.choice(penzerme)

kerdes = input("Fej vagy írás? ")
print(f"A gép erre gondolt: {dobas}")

if kerdes == dobas:
    print("Eltaláltad!")
else:
    print("Nem sikerült.")