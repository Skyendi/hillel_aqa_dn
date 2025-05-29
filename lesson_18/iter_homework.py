my_list: list[int] = [10, 20, 30, 40, 50]


def reverse_iterator(*args) -> iter:
    args = iter(my_list[::-1])
    return args


reverse_it: iter = reverse_iterator(my_list)

print(next(reverse_it))
print(next(reverse_it))
print(next(reverse_it))
print(next(reverse_it))
print(next(reverse_it))

# _________________________________________________________________________________________
print("_" * 70)


def get_iter_in_range(n: int) -> iter:
    iter_range = (i for i in range(n) if i % 2 == 0)

    return iter(iter_range)


even_it: iter = get_iter_in_range(10)

print(next(even_it))
print(next(even_it))
print(next(even_it))
print(next(even_it))
print(next(even_it))
