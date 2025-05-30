def create_list_of_even_nums(n: int) -> list[int]:
    even_numbers_gen = (i for i in range(n) if i % 2 == 0)
    list_of_even = []
    for num in even_numbers_gen:
        list_of_even.append(num)

    return list_of_even


print(create_list_of_even_nums(11))


# __________________________________________________________________________________


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_func(n) -> list[int]:
    fibonacci = fibonacci_generator()
    result = []
    for i in range(n):
        result.append(next(fibonacci))
    return result


print(fibonacci_func(20))
