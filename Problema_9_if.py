'''Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze
câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând
numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor. Exemplu: Date de intrare Nr. bile albe mici: 2
Nr. bile albe mari: 3 Nr. bile rosii mici: 1 Nr. bile rosii mari: 4 Nr. bile verzi mici: 3 Nr. bile verzi mari: 4 Date de ieşire Totalul
bilelor: 17 Mari: 11 bile Verzi: 7 bile .'''
xa=int(input('Numarul de bile albe mari:'))
xr=int(input('Numarul de bile rosii mari:'))
xv=int(input('Numarul de bile verzi mari:'))
ya=int(input('Numarul de bile albe mici:'))
yr=int(input('Numarul de bile rosii mici:'))
yv=int(input('Numarul de bile verzi mici:'))
tx=xa+xr+xv
ty=ya+yr+yv
print("Numarul total de bile:", tx+ty, "bile")
if (tx>ty):
    print("Mai multe sunt bile mari:",tx, "bile")
if (ty>tx):
    print("Mai multe sunt bile mici:",ty, "bile")
if (tx==ty):
    print("Numarul de bile mari si mici este egal:",ty, "bile")
if ((xa+ya>xr+yr) and (xa+ya>xv+yv)):
    print("Cele mai numeroase sunt bilele albe:", xa+ya, "bile")
if ((xr+yr>xa+ya) and (xr+yr>xv+yv)):
    print("Cele mai numeroase sunt bilele rosii:", xr+yr, "bile")
if ((xv+yv>xr+yr) and (xv+yv>xa+ya)):
    print("Cele mai numeroase sunt bilele verzi:", xv+yv, "bile")