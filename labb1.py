import math
print('Här kan du räkna ut volymen för en liksidig kub samt en liksidig tetrahedron: ')
var1 = (input("Ange längden i centimeter för en av figurens sidor: "))
var1 = float(var1.replace(',', '.'))
kub = round((var1 * var1 * var1), 2)
sqrtroot = math.sqrt(12)
tetra =round((kub /6), 2)
print('Om sidan på en liksidig kub är ', var1, 'cm. ', 'Så är volymen', kub, 'cm3')
print('Om sidan på en liksidig tetraeder är ', var1, 'cm.', 'Så är volymen')
