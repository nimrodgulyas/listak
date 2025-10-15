honapok = ['január', 'február', 'március', 'április', 'május', 'június']

# a lista végére hozzáfűz egy elemet
honapok.append('július')
print(honapok)


# eltávolítja a legutolsó elemet, és azzal tér vissza
# itt például a törölt értéket a 'torolt_nyelv' fogja tartalmazni
print(honapok.pop())
print(f'Utolsó hónap törlése után a lista:\n {honapok}')
torolt_honap = honapok.pop()
print(f'Utolsó hónap: {torolt_honap}')
print(honapok)

# törlés adott index alapján
torolt_honap = honapok.pop(0)
print(torolt_honap)
print(honapok)

print(honapok.remove('február'))
print(honapok)
honapok.insert(0,'február')
print(honapok)

# lista kiürítése
honapok.clear()
print(honapok)