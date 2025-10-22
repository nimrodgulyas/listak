mindkettovel_oszthato = []
for i in range(1,100):
    if i % 3 == 0 and i % 5 ==0:
        mindkettovel_oszthato.append(i)

csak_harommal_oszthato = []
for b in range(1,100):
    if b % 3 == 0 and b % 5 != 0:
        csak_harommal_oszthato.append(b)
    if b % 3 == 0 and b % 5 ==0:
        csak_harommal_oszthato.append(b)

csak_ottel_oszthato = []
for a in range(1,100):
    if a % 3 != 0 and a % 5 == 0:
        csak_ottel_oszthato.append(a)
    if a % 3 == 0 and a % 5 == 0:
        csak_ottel_oszthato.append(a)

print(f'5-tel és 3-mal is osztható számok: {mindkettovel_oszthato}')
print(f'Csak 3-mal osztható számok: {csak_harommal_oszthato}')
print(f'Csal 5-tel osztható számok: {csak_ottel_oszthato}')