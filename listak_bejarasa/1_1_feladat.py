"""
1. Feladat
Készíts egy programot, amely [1; 40] intervallumon kiírja a 3-mal osztható számokat!
"""
szamok = []
for i in range(1,41):
    if i % 3 == 0:
        szamok.append(i)

print(szamok)