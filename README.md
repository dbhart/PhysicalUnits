# PyUnits
Physical units for scientific and engineering

This is a simple implementation of a units framework for python, and can be expanded upon as desired.

Use:

from units import C

#assign units to a number - in this case 10 lbf of force:
F = 10*C.LBF

report the number in units force:
print( F/C.LBF )

report the number in units of Newtons:
print ( F/C.N )

assign a mixed unit to a value in this case density in SI units:
rho = 10 *C.KG/C.M**3

report the unit is US customary units:
print ( rho / (C.SLUG/C.FT**3) )
