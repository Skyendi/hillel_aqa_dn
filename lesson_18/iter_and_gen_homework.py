def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci = fibonacci_generator()

for i in range(20):
    print(next(fibonacci))
# ______________________________________________________________________
n = 11
even_numbers_gen = (i for i in range(n) if i % 2 == 0)

for num in even_numbers_gen:
    print(num)
# __________________________________________________________________________________

my_list = [10, 20, 30, 40, 50]

reverse_iterator = iter(my_list[::-1])

print(next(reverse_iterator))
print(next(reverse_iterator))
print(next(reverse_iterator))
print(next(reverse_iterator))
print(next(reverse_iterator))


# _________________________________________________________________________________________

def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


for num in even_numbers(10):
    print(num)
