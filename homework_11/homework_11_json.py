import json
from pathlib import Path
import logging
from homework_11.my_file_logger import logger

file_path_localizations_en = Path("json_files/localizations_en.json")
file_path_localizations_ru = Path("json_files/localizations_ru.json")
file_path_login = Path("json_files/login.json")
file_path_swagger = Path("json_files/swagger.json")

list_of_path_real = [file_path_localizations_en, file_path_localizations_ru, file_path_login, file_path_swagger]


def validation_of_json(list_of_path):
    for file_path in list_of_path:
        file_path = file_path
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                print(f"The {file_path.name} is validates successfully")
        except json.JSONDecodeError:
            logger.error(f"{file_path.name} is invalid - fault: json.JSONDecodeError ")








validation_of_json(list_of_path_real)
