import math
start = -5.0
end = 5.0
step = 0.5

print("-" * 30)
print(f"{'x':>8} | {'y':>10}")
print("-" * 30)
x = start
while x <= end + 0.0001: 
    if x < 0:
        y = x**2
    elif 0 <= x <= 2:
        y = math.sqrt(x)
    else: # x > 2
        y = math.log(x) if x > 0 else float('nan')
    print(f"{x:8.1f} | {y:10.4f}")
    x += step
print("-" * 30)