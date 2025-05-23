n = 11


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


def validation_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            print("Arguments should be int")

    return wrapper


@validation_decorator
@log_decorator
def even_numbers(n):
    even_list = [i for i in range(n) if i % 2 == 0]
    return even_list


even_numbers(n)
