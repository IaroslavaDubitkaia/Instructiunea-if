'''Se introduc trei date de forma număr curent elev, punctaj. Afişaţi numărul elevului cu cel mai mare punctaj. Exemplu : Date de
intrare nr crt 7 punctaj 120 nr crt 3 punctaj 100 nr crt 4 punctaj 119 Date de ieşire punctaj maxim are elevul cu nr crt 7.'''
n1=int(input('Numarul curent elev 1:'))
n2=int(input('Numarul curent elev 2:'))
n3=int(input('Numarul curent elev 3:'))
p1=int(input('Punctaj elev 1:'))
p2=int(input('Punctaj elev 2:'))
p3=int(input('Punctaj elev 3:'))
if (p1>p2) and (p1>p3):
    print("Puctaj maxim are elevul cu numarul curent ", n1)
if (p2>p1) and (p2>p3):
    print("Puctaj maxim are elevul cu numarul curent ", n2)
if (p3>p1) and (p3>p2):
    print("Puctaj maxim are elevul cu numarul curent ", n3)
if (p1==p2) and (p1>p3) and (p2>p3):
    print("Puctaj maxim are elevul cu numarul curent ", n1)
if (p1==p3) and (p1>p2) and (p3>p2):
    print("Puctaj maxim are elevul cu numarul curent ", n3)
if (p3==p2) and (p2>p1) and (p3>p1):
    print("Puctaj maxim are elevul cu numarul curent ", n2)