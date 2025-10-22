"""
3. Feladat
Az adott lista (→ 'Próbáld ki!') elemei közül a program kiírja a 3-mal osztható páros számokat!
"""
harommal_oszthato_szamok = []
for i in range(1,40):
    if i % 3 == 0 and i % 2 == 0:
        harommal_oszthato_szamok.append(i)
print(f'3-mal osztható páros számok: {harommal_oszthato_szamok}')