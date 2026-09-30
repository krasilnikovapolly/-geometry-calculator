import math
x = 1.5
numerator = 2 * (x**2) - 4
denominator = math.exp(-2 * x) - math.tan(1 - 2**x)
part1 = numerator / denominator
arcsin_arg = 2 * x - math.sqrt(1 + 2 * x)
part2 = math.asin(arcsin_arg)
y = part1 + part2
print(f"Значение y = {y:.5f}")