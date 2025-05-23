my_list = [10, 20, 30, 40, 50]

reverse_iterator = iter(my_list[::-1])

print(next(reverse_iterator))
print(next(reverse_iterator))
print(next(reverse_iterator))
print(next(reverse_iterator))
print(next(reverse_iterator))

# _________________________________________________________________________________________
print("_" * 70)


def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


for num in even_numbers(10):
    print(num)
