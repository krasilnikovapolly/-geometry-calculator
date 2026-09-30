a = 10
b = 25
result = a + b
print("Первое число:", a)
print("Второе число:", b)
print("Сумма двух чисел:", result)
if a > 0 and a % 2 == 0:
    print(f"Число {a} является положительным и четным")
else:
    print("Число не является положительным либо четным")
if 100 <= a <= 999:
    print(f"Число {a} является трёхзначным")
else:
    print(f"Число {a} не является трёхзначным")
maximum = max(a, b, result)
print(f"Наибольшее из чисел {a}, {b}, {result}: {maximum}")