honapok = ['január', 'február', 'március', 'április', 'május', 'június']

print(type(honapok))

#lista hossza: len()
print(len(honapok))

# a 0. indexű az első elem
print(honapok[0])
print(honapok[1])
print(honapok[2])

#hátulról az első, vagyis az utolsó elem
print(f'Utolsó elem a listában: {honapok[-1]}')

# az 1-es és 2-es indexű elemek kiíratása
print(honapok[1:3])

# az elejétől a 2-es indexű elemmel bezárólag
print(honapok[:3])

# 2-es indexű elemtől a végéig
print(honapok[2:])

#join(): a lista elemeit egy sztriggé fűzi össze
# a megadott elválasztó karakterekkel tagolva
print(', '.join(honapok))

#lista bejárása for range ciklussal
for i in range(len(honapok)):
    print(honapok[i])

# lista bejárása for - items
print('\nHónapok\n')
for honap in honapok:
    print(honap)