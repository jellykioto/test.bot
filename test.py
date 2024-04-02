a = -3
b = 4
c = 4
d = (b ** 2 - 4 * a * c) ** 0.5
rez = (-b + d) / 2 * a
rez1 = (-b - d) / 2 * a

print(f'd={d}')
print(rez // rez1)