import math

print('\n ****************************************************************************')
print(' Här kan du räkna ut volymen för en liksidig kub och en liksidig tetrahedron')
print(' ****************************************************************************\n')

var1 = (input("Ange längden på en av figurens sidor (i cm): "))
var1 = float(var1.replace(',', '.'))
volumeCube = var1 ** 3
volumeTetra = volumeCube/(6 * math.sqrt(2))

print('Om det är en kub så är volymen ', volumeCube, 'cm3')
print('Om det är en tetrahedron så är volymen', volumeTetra, 'cm3')
