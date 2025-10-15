import math

# 1. Adottak a téglalap alapélei. Írassa ki az oldalakat és a kerületet, területet!

aoldal = 4
boldal = 2
print("aoldal", aoldal)
print("boldal", boldal)
print("terulet" , aoldal*boldal)
print("kerulet" , (aoldal+boldal)*2)


# 2. Legyen megadva a kör sugara alapértéknek. Számolja ki a kör átmérőjét, kerületét, területet!

korsugara = 2
koratmero  = (2*korsugara)
korkerulet = (2*math.pi*korsugara)
korterulet = (math.pi*(korsugara*korsugara))

print(2*korsugara)
print(2*math.pi*korsugara)
print(2*math.pi*(korsugara*korsugara))