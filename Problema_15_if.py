'''Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. Radu este pe locul x în ordinea mediilor. În
ce clasa va fi repartizat (A, B, C, D sau E)?. Exemplu : date de intrare : x=73 date de ieşire : C.'''
x=int(input('Locul pe care se afla Radu:'))
nc=x//25
if x%25!=0:
    nc=1
if (nc<=5):
    if nc==1:
        print("El va fi in clasa A")
    elif nc==2:
        print("El va fi in clasa B")
    elif nc==3:
        print("El va fi in clasa C")
    elif nc==4:
        print("El va fi in clasa D")
    else:
        print("El va fi in clasa E") 
else:
    print("Nu mai sunt clase disponibile")


