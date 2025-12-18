def km_to_m(km):
    return km * 1000

def m_to_cm(m):
    return m * 100

def cm_to_mm(cm):
    return cm * 10

def ft_to_in(ft):
    return ft * 12

def in_to_cm(inch):
    return inch * 2.54

def distance_converter(value, conversion, func):
    result = func(value)
    print(f"{conversion}: {result}")

d = float(input("Enter distance value: "))

distance_converter(d, "km to m", km_to_m)
distance_converter(d, "m to cm", m_to_cm)
distance_converter(d, "ft to in", ft_to_in)
distance_converter(d, "in to cm", in_to_cm)
