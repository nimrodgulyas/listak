"""
A program tároljon egy listában színeket. 
Kérjen be a felhasználótól egy színt,
és állapítsa meg, hogy a megadott szín már szerepel-e
az adott listában. A vizsgálat eredményéről tájékoztassa
a program a felhasználót, és írja ki egymás mellé
vesszővel elválasztva a lista által tartalmazott
színeket!
"""
"""1.2 Feladat
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást, hogy pontosan hányszor szerepel a felhasználó
által megadott szín a listában! Ha a megadott szín nincs még tárolva, továbbra is a "A megadott szín nem szerepel a listában." szöveg jelenjen meg!
"""


szinek = ['kék', 'zöld', 'piros', 'sárga', 'piros']
szin = str(input('Adj meg egy színt!: '))
if szin in szinek:
    print(f'Szerepel a listában a szín! {szinek.count(szin)}x')
else:
    print(f'A megadott szín nem szerepel a listában. A lista színei: {szinek}')