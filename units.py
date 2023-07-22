# PyUnits
# Physical units for scientific and engineering This is a simple implementation of a units framework for python, and can be expanded upon as desired.
# Use:
# from units import C
# assign units to a number - in this case 10 lbf of force:
# F = 10*C.LBF
# report the number in units force:
# print( F/C.LBF )
# report the number in units of Newtons:
# print ( F/C.N )
# assign a mixed unit to a value in this case density in SI units:
# rho = 10 *C.KG/C.M**3
# report the unit is US customary units:
# print ( rho / (C.SLUG/C.FT**3) )

class C():
    from math import pi as mypi
    # angles
    DEG = mypi/180.
    ARCMIN = mypi/180/60
    ARCSEC = mypi/180/360
    RAD = 1.

    # mass
    SLUG = 1.
    SLINCH = 12.
    KG = 1/14.5939
    GM = 1/14593.9

    # length
    FT = 1.
    IN = 1./12.
    M = 1000./25.4/12.
    CM = 10/25.4/12
    MM = 1/25.4/12
    MILE = 5280.
    NM = 6076

    # time
    SEC = 1.
    MILISEC = 1.0e-3
    MICROSEC = 1.0e-6
    MIN = 60.
    HOUR = 3600.
    DAY = 3600*24.
    YEAR = 3600*24.*365

    # speed
    FPS = 1.
    MPH = 5280./3600.
    KNOT = 6076./3600.

    # force
    LBF = 1.
    N = 0.22480894387096
    KN = 224.80894387096

    # gravitational constant
    G0 = 32.174
    LBM = 1/32.174

    # pressure
    PSI = 144.
    KSI = 144.0e3
    MSI = 144.0e6
    PSF = 1.
    PA = 20.89/1000

    # # temperature
    # K = -273.15
    # C = 1.
    # F = 9./5.+32.
    # R = 9./5.+32+459.67