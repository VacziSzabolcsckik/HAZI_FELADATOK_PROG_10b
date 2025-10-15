import math

# 3. feladat
a = 3
b = 4
c = 5

kerulet = a + b + c
s = kerulet / 2
terulet = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("3. feladat - Háromszög")
print("Oldalak:", a, b, c)
print("Kerület:", kerulet)
print("Terület:", round(terulet, 2))
print()


# 4. feladat
oldal = 6
magassag = (math.sqrt(3) / 2) * oldal

print("4. feladat - Szabályos háromszög")
print("Oldal:", oldal)
print("Magasság:", round(magassag, 2))
print()


# 5. feladat
el = 5
lapatlo = el * math.sqrt(2)
testatlo = el * math.sqrt(3)

print("5. feladat - Kocka")
print("Él:", el)
print("Lapátló:", round(lapatlo, 2))
print("Testátló:", round(testatlo, 2))