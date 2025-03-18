alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"\
That depends a good deal on where you want to get to," said the Cat.\n"I don\'t \
    much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," \
    said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, \
    you\'re sure to do that," said the Cat, "if you only walk long enough."'
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print(f"Total area of both seas is {total_area} km2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_qty = 375291
storage_1: int = total_qty - 222950
storage_3: int = total_qty - 250449
storage_2: int = total_qty - (storage_1 + storage_3)
print(f"in first storage - {storage_1}, \nin second storage {storage_2}, \nin third storage {storage_3}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month_payment: int = 1179
total_payment: int = 18 * month_payment
print(f"The computer cost {total_payment}")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
print(a)
b = 9907 % 9
print(b)
c = 2789 % 5
print(c)
d = 7248 % 6
print(d)
e = 7128 % 5
print(e)
f = 19224 % 9
print(f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizzas: float = 4 * 274
middle_pizzas: float = 2 * 218
juice: float = 4 * 35
cake: float = 350
water: float = 3 * 21
total = big_pizzas + middle_pizzas + juice + cake + water
print(f" Irinka will spend {total} uah")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_qty: int = 232
page_capacity: int = 8
total_pages = photo_qty / page_capacity
print(f"Igor needs {total_pages} pages")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distace = 1600
fuel_consumption_per_100_km = 9
fuel_tank_capacity = 48
total_fuel = (1600 / 100) * 9
fuel_top_ups = total_fuel / fuel_tank_capacity
print(f"Family will spend {total_fuel} l of petrol")
print(f"Family need to top up petrol {fuel_top_ups} times")