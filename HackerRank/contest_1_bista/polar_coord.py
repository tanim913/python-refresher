from math import atan2

z = complex(input())

x = z.real
y = z.imag

r = (x**2+y**2)**.5
phi = atan2(y, x)  # tan inverse y/x

print(r)
print(phi)
