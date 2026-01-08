import random

shrek=random.randint(6,6*18)
osszegshrek = 0
while shrek %6!=0:
    shrek = random.randint(6,18*6)
print(shrek)
for shuz in range(shrek):
    shrekhuz = random.randint(100,999)
    while shrekhuz %20!=0:
        shrekhuz = random.randint(100,999)
    osszegshrek += shrekhuz
    print(shrekhuz)

print("Shrek ennyit húzott: ",osszegshrek, "ennyit dobott az úr: ", shrek )



fiona=random.randint(6,6*18)
osszegfiona = 0
while fiona %6!=0:
    fiona = random.randint(6,18*6)
print(fiona)
for fhuz in range(fiona):
    fionahuz = random.randint(100,999)
    while fionahuz %20!=0:
        fionahuz = random.randint(100,999)
    osszegfiona += fionahuz
    print(fionahuz)

print("Fiona ennyit húzott: ",osszegfiona, "ennyit dobott a hölgy: ", fiona )

if osszegshrek > osszegfiona:
    print("Fióna nyert!")
elif osszegshrek < osszegfiona:
    print("Shrek nyert!")
else:
    print("Döntetlen!")


#2. feladat

shrekhuzas = 0
while shrekhuzas != 30:
    shreklap = chr(random.randint(65,90))
    shrekhuzas+=1
    print(shreklap, end=" ")

print(shreklap)

fionahuzas = 0
while fionahuzas != 30:
    fionalap = chr(random.randint(65,90))
    fionahuzas+=1
    print(fionalap, end=" ")

print(fionalap)