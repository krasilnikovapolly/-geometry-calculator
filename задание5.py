import math
product = 1.0

for n in range(1, 21):  
    term = (n**2) + math.sin(n) + 1
    product *= term

print(f"Произведение = {product:.5e}") 