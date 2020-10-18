'''Să se afişeze cel mai mare număr par dintre doua numere introduse în calculator. Exemple : Date de intrare 23 45 Date de
ieşire nu exista numar par ; Date de intrare 28 14 Date de ieşire 28 ; Date de intrare 77 4 Date de ieşire 4.'''
a=int(input('Primul numar:'))
b=int(input('Al doilea numar:'))
if (a%2==0) and (b%2==0):
    if (a>b):
        print("Cel mai mare numar par este", a)
    if (b>a):
        print("Cel mai mare numar par este", b)
if (a%2==0) and (b%2!=0):
    print("Cel mai mare numar par este", a)
if (a%2!=0) and (b%2==0):
    print("Cel mai mare numar par este", b)
if (a%2!=0) and (b%2!=0):
    print("Nu sunt numere pare")
