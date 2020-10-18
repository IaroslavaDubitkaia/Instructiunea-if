'''Andrei primeşte într-o zi trei note, nu toate bune. Se hotărăşte ca, dacă ultima notă este cel puţin 8, să le spună părinţilor toate
notele primite iar dacă este mai mică decât 8, să le comunice doar cea mai mare notă dintre primele două. Introduceţi notele
luate şi afişaţi notele pe care le va comunica părinţilor. Exemple : Date de intrare 6 9 9 Date de ieşire 6 9 9 ; Date de
intrare 8 5 7 Date de ieşire 8.'''
a=int(input('Prima nota este '))
b=int(input('A doua nota este '))
c=int(input('A treia nota este '))
if (c>=8):
    print("Notele spuse parintilor sunt", a, b, c)
if (c<8):
    if (a>b):
        print("Nota spusa parintilor este", a)
    if (b>a):
        print("Nota spusa parintilor este", b)
    if (a==b):
        print("Nota spusa parintilor este", a)