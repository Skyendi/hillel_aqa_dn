list_of_string: list[str] = ["1, 2, 3, 4", "1, 2, 3, 4, 50", "qwerty1, 2, 3"]


def sum_from_list_of_strings(*args: list[str]):
    for items in args:
        try:
            nums_sum = sum([int(i) for i in items.split(",")])

            print(nums_sum)
        except ValueError:
            print("I can't to do this")


sum_from_list_of_strings(*list_of_string)
