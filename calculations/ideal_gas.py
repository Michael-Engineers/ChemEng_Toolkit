#PV = nRT
#n = PV/RT where R = 8.314, P in Pascals, V in m^3 and T in Kelvin


r = 8.314 #J/Kmol


def ideal_gas_moles(p,v,t):
    return (p*v)/(r*t)

def ideal_gas_pressure(n,v,t):
    return (n*r*t)/v

def ideal_gas_temperature(p,v,n):
    return (p*v)/(r*n)

def ideal_gas_volume(p,t,n):
    return (n*r*t)/p


