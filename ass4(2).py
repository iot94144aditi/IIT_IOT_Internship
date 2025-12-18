km_to_m = lambda km: km * 1000
m_to_cm = lambda m: m * 10
cm_to_mm = lambda cm: cm * 10
ft_to_in = lambda ft: ft * 12
in_to_cm = lambda inch: inch * 2.54

def distance_converter(value, conversion, func):
    print(f"{conversion}: {func(value)}")

d = float(input("Enter distance value: "))

distance_converter(d, "km to m", km_to_m)
distance_converter(d, "m to cm", m_to_cm)
distance_converter(d, "cm to mm", cm_to_mm)
distance_converter(d, "ft to in", ft_to_in)
distance_converter(d, "in to cm", in_to_cm)
