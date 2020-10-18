'''Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane,
exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi. Exemplu : Date
de intrare data curenta 2005 10 25 data nasterii 1960 11 2 Date de ieşre 44 ani.''' 
dc=int(input('Data curenta:'))
lc=int(input('Luna curenta:'))
ac=int(input('Anul curenta:'))
dn=int(input('Data nasterii:'))
ln=int(input('Luna nasterii:'))
an=int(input('Anul nasterii:'))
if (lc>ln):
    print(ac-an, "ani")
if (lc<ln) or ((lc==ln) and (dn>dc)):
    print((ac-an)-1, "ani")