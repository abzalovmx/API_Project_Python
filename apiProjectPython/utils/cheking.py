""" Методы для проверки ответов наших запросов """
from requests import Response
import json

class Checking():

    """ Метод для проверки статус кода """
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"Успешно!!! Статус код = {response.status_code}")
        else:
            print(f"Провал!!! Статус код = {response.status_code}")

    """ Метод для проверки наличия обязательных полей в ответе запроса """
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """ Метод для проверки значений объязательных полей в ответе запроса """
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'{field_name} верен!!!')

    """ Метод для проверки значений объязательных полей в ответе запроса по заданному слову """
    @staticmethod
    def check_json_searche_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f'Слово {search_word} присутсвует')
        else:
            print(f'Слово {search_word} отсутсвует')


