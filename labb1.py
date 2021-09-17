import math

print('\n ****************************************************************************')
print(' Här kan du räkna ut volymen för en liksidig kub och en liksidig tetrahedron')
print(' ****************************************************************************')

var1 = (input("Ange längden på en av figurens sidor (i cm): "))
var1 = float(var1.replace(',', '.'))
volumeCube = var1 ** 3
volumeTetra = var1 ** 3/6*math.sqrt(2)

print('Kubens volym', volumeCube, 'cm3')
print('Tetraeders volym', volumeTetra, 'cm3')
