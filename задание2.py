import math
a = -0.1
b = 0.7
step = 0.05

print("-" * 30)
print(f"{'x':>8} | {'y':>10}")
print("-" * 30)

n_steps = int((b - a) / step) + 1

for i in range(n_steps):
    x = a + i * step
    if x <= 0:
        y = float('nan') 
    else:
        try:
            term1 = math.sin(x**x)
            term2 = 2 * (x**2)
            term3 = (3**x) * math.sin(3 * x)
            y = term1 - term2 + term3
        except ValueError:
            y = float('nan')

    print(f"{x:8.2f} | {y:10.4f}")

print("-" * 30)