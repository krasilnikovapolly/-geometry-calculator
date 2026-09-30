total_sum = 0.0
for n in range(2, 101): 
    term = n / (2 * n + 1)
    total_sum += term
print(f"Сумма = {total_sum:.5f}")