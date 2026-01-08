szo1 = "alma"
szo2 = "alkat"
kulonbseg = 0
minimumhossz = 0

if len(szo1) > len(szo2):
    minimumhossz = len(szo2)
else:
    minimumhossz = len(szo1)

for i in range(0, minimumhossz, 1):
    if szo1[i] != szo2[i]:
        kulonbseg += 1

if len(szo1) > len(szo2):
    kulonbseg += len(szo1) - len(szo2)
else:
    kulonbseg += len(szo2) - len(szo1)

print(kulonbseg)