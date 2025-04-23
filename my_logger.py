# import logging
#
# # Створення логера
# logger = logging.getLogger("log_event")
#
# # Налаштування рівня логування
# logger.setLevel(logging.INFO)
#
# # Створення обробника для запису в файл
# file_handler = logging.FileHandler('login_system.log')
#
# # Налаштування рівня логування для обробника
# file_handler.setLevel(logging.INFO)
#
# # Створення форматера для обробника
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
#
# # Додавання обробника до логера
# logger.addHandler(file_handler)