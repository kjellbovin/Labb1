import math
print('\n ****************************************************************************')
print(' Här kan du räkna ut volymen för en liksidig kub och en liksidig tetrahedron')
print(' ****************************************************************************')

var1 = (input("Ange längden på en av figurens sidor (i cm): "))
var1 = float(var1.replace(',', '.'))
kub = round((var1 ** 3), 2)
tetra = round(math.sqrt(kub /6), 2)

print('Kubens volym', kub, 'cm3')
print('Tetraeders volym', tetra, 'cm3')
