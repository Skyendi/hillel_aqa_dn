def evens_sum(list_of_numbers):
    even_sum = 0
    for num in list_of_numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum


def average_value(nums):
    nums = [arg for arg in nums if isinstance(arg, (int, float))]

    average = sum(nums) / len(nums)
    return average


def sum_calc(a, b):
    sum_result = a + b
    return sum_result


def check_email(email):
    if "@" not in email or "." not in email:
        return False
    else:
        return True


def check_age(age:int):
    if age < 18:
        return "You are not allowed!"
    elif age >= 18:
        return "You are allowed!!!"
