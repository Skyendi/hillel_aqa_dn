numbers = [68, 1, 18, 79, 29, 76, 89, 87, 81, 1, 5, 9, 24, 4, 19, 75, 20, 32, 22, 47]
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num

print(even_sum)