print('\n ****************************************************************************')
print(' Här kan du räkna ut volymen för en liksidig kub och en liksidig tetrahedron')
print(' ****************************************************************************')

var1 = (input("Ange längden på en av figurens sidor (i cm): "))
var1 = eval(var1.replace(',', '.'))
kub = round((var1 ** 3), 2)
tetra = round((kub*(0.5 / 12) * kub), 2)

print('Kubens volym', kub, 'cm3')
print('Tetraeders volym', tetra, 'cm3')
