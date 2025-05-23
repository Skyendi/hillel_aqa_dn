n = 11
even_numbers_gen = (i for i in range(n) if i % 2 == 0)

for num in even_numbers_gen:
    print(num)

print("_" * 70)


# __________________________________________________________________________________


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci = fibonacci_generator()

for i in range(20):
    print(next(fibonacci))
