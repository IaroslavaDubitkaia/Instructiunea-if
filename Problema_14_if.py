'''Într-o tabără, băieţii sunt cazaţi câte 4 într-o căsuţă, în ordinea sosirii. Ionel a sosit al n-lea. În a câta căsuţă se va afla?
Exemplu : date de intrare : n=69 date de ieşire : casuta 17.'''
n=int(input('Numarul ordinii de sosire a lui Ionel:'))
if (n>4):
    print("El va fi cazat in casuta numarul", n//4)
if (n<=4):
    print("El va fi cazat in casuta numarul 1")