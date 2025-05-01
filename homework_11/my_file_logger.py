import logging

# Створення логера
logger = logging.getLogger(__name__)

# Налаштування рівня логування
logger.setLevel(logging.INFO)

# Створення обробника для запису в файл
file_handler = logging.FileHandler('json_nedilko.log')

# Налаштування рівня логування для обробника
file_handler.setLevel(logging.DEBUG)

# Створення форматера для обробника
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Додавання обробника до логера
logger.addHandler(file_handler)


