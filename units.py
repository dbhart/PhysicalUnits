# PyUnits
# Physical units for scientific and engineering This is a simple implementation of a units framework for python, and can be expanded upon as desired. These conversions are implemented in an easy-to-read format, which may add additional computation time, in python, when used in operations that involve many computations.
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
    from math import pi
    # angles - ref radians
    DEG = pi/180.
    ARCMIN = pi/180./60.
    ARCSEC = pi/180./360.
    RAD = 1.
    
    #periodic rate ref - rad/sec
    HZ = 1./2./pi
    DPS = 180./pi
    RPM = 60./2./pi

    # mass - ref slug
    SLUG = 1.
    SLINCH = 12.
    KG = 1./14.5939
    GM = 1./14593.9

    # length - ref ft
    FT = 1.
    IN = 1./12.
    M = 1000./25.4/12.
    CM = 10./25.4/12.
    MM = 1./25.4/12.
    MILE = 5280.
    NM = 6076.

    # time - ref sec
    SEC = 1.
    MILISEC = 1.0e-3
    MICROSEC = 1.0e-6
    MIN = 60.
    HOUR = 3600.
    DAY = 3600.*24.
    YEAR = 3600.*24.*365.

    # speed - ref fps
    FPS = 1.
    MPH = 5280./3600.
    KNOT = 6076./3600.

    # force - ref pound-force
    LBF = 1.
    N = 0.22480894387096
    KN = 224.80894387096

    # gravitational constant - ref earth surface gravity in ft/sec2
    G0 = 32.174
    LBM = 1./32.174

    # pressure - ref lbf/ft2
    PSI = 144.
    KSI = 144.0e3
    MSI = 144.0e6
    PSF = 1.
    PA = 20.89/1000.

    # temperature !!To be later implemented - this unit requires a DC offset, which would require a modification of
    # python std operotors to implement in its given syntax!!
    # K = -273.15
    # C = 1.
    # F = 9./5.+32.
    # R = 9./5.+32+459.67