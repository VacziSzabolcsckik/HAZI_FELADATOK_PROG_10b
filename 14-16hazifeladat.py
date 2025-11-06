# 14. Feladat
szo = input("Írj egy szót:")
print(szo)
if szo:
    utolso = ""
    for karakter in szo:
        utolso = karakter
    print(utolso)
# 15. Feladat
if szo:
    elso = ""
    utolso = ""
    elsokar =  False
    for karakter in szo:
        if not elsokar:
            elso = karakter
            elsokar = True
        utolso = karakter
    if elso == utolso:
        print("Megegyezik az utolsó és első karakter: Igen")
    else:
        print("Megegyezik az utolsó és első karakter: Nem")

# 16. Feladat
szoveg = input("Adj meg egy szöveget: ")
masodik = ""

szam = 0
for mbetu in szoveg:
    if szam % 2 == 0:
        masodik += mbetu
    szam += 1

print("Minden második betű:", masodik)