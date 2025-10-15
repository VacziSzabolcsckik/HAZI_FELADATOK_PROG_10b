import math

# 1. feladat
aoldal = 4
boldal = 2
print("1. feladat")
print("aoldal", aoldal)
print("boldal", boldal)
print("terulet" , aoldal*boldal)
print("kerulet" , (aoldal+boldal)*2)


# 2. feladat
korsugara = 2
koratmero  = (2*korsugara)
korkerulet = (2*math.pi*korsugara)
korterulet = (math.pi*(korsugara*korsugara))

print("2. feladat")
print(2*korsugara)
print(2*math.pi*korsugara)
print(2*math.pi*(korsugara*korsugara))

# 3. feladat
a = 3
b = 4
c = 5

kerulet = a + b + c
s = kerulet / 2
terulet = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("3. feladat")
print("Oldalak:", a, b, c)
print("Kerület:", kerulet)
print("Terület:", round(terulet, 2))
print()


# 4. feladat
oldal = 6
magassag = (math.sqrt(3) / 2) * oldal

print("4. feladat")
print("Oldal:", oldal)
print("Magasság:", round(magassag, 2))
print()


# 5. feladat
el = 5
lapatlo = el * math.sqrt(2)
testatlo = el * math.sqrt(3)

print("5. feladat")
print("Él:", el)
print("Lapátló:", round(lapatlo, 2))
print("Testátló:", round(testatlo, 2))

# 6. feladat

print("6. feladat")
vezeteknev = input("Vezetéknév: ")
keresztnev = input("Keresztnév: ")
print("Teljes név:", vezeteknev + " " + keresztnev)

# 7. feladat

print("7. feladat")
szam = int(input("Adj meg egy egész számot: "))
if szam % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")

# 8. feladat

print("8. feladat")
jegy = int(input("Add meg az érdemjegyet (1-5): "))
if jegy == 1:
    print("Elégtelen")
elif jegy == 2:
    print("Elégséges")
elif jegy == 3:
    print("Közepes")
elif jegy == 4:
    print("Jó")
elif jegy == 5:
    print("Jeles")
else:
    print("Hiba!")

# 9. feladat

print("9. feladat")
hofok = float(input("Add meg a víz hőfokát °C-ban: "))
if hofok <= 0:
    print("Szilárd")
elif hofok < 100:
    print("Folyékony")
else:
    print("Gáz")

# 10. feladat

print("10. feladat")
a = float(input("Add meg az első oldalt: "))
b = float(input("Add meg a második oldalt: "))
c = float(input("Add meg a harmadik oldalt: "))
if a + b > c and a + c > b and b + c > a:
    print("A háromszög szerkeszthető.")
else:
    print("A háromszög nem szerkeszthető.")

# 11. feladat

print("11. feladat")
f = float(input("Add meg a hőmérsékletet Fahrenheitben: "))
c = (f - 32) * 5 / 9
print(str(f) + "°F = " + str(round(c, 2)) + "°C")


# 12. feladat

print("12. feladat")
c = float(input("Add meg a hőmérsékletet Celsiusban: "))
f = c * 9 / 5 + 32
print(str(c) + "°C = " + str(round(f, 2)) + "°F")

# 13. feladat

print("13. feladat")
masodperc = int(input("Add meg az időt másodpercben: "))
ora = masodperc // 3600
maradek = masodperc % 3600
perc = maradek // 60
masodperc = maradek % 60
print(str(ora) + " óra, " + str(perc) + " perc, " + str(masodperc) + " másodperc")