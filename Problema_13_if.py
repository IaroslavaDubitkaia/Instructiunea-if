'''La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această
secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi? Exemplu : date de intrare : x=38 date de ieşire :
rosie.'''
x=int(input('Locul pe care este Ionel:'))
if (x<=100):
    if (x%4==1):
        print("Ionel va primi tricou alb")
    elif (x%4==2):
        print("Ionel va primi tricou rosu")
    elif (x%4==3):
        print("Ionel va primi tricou albastru")
    else:
        print("Ionel va primi tricou negru")
else:
    print("Ionel nu va primi tricou")