#
"""Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e! A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!
"""

valasz = input('Jó napod van?  ')
valasz_lowercase = valasz.lower()
if valasz_lowercase == "igen":
     print("Örülök hogy jó napod van!")
elif valasz == "nem":
    print("oke")
else:
    print("Sajnos nem értem a vlaszodat!")
