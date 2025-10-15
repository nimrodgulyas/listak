import random
"""
2. Feladat
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre!
A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, és a program törölje ennek a számnak valamennyi előfordulását a listából,
majd írja ki a módosított listát a képernyőre!

"""
szamlista = []
for i in range(1,11):
    # print(i)
    random_number = random.randint(1,3)
    szamlista.append(random_number)
    # szamlista.insert(i, random_number)

print(f'A lista elemei: {szamlista}')
szam = int(input('Adj meg egy számot 1 és 3 között!: '))
while szam in szamlista: 
    szamlista.remove(szam)
print(f'Módosított lista: {szamlista}')
