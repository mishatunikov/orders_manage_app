import re


def is_text(string: str) -> bool:
    """
    Проверяет строку на то, состоит ли она только из букв и пробелов.

    Parameters:
        string: str. Строка текста.
    """
    if re.fullmatch(r'^[а-яА-Яa-zA-Z ]+', string):
        return True


def is_number(string: str) -> bool:
    """
    Проверяет строку на то, является ли она корректным числом.

    Parameters:
    string: str. Строка текста.
    """
    if re.fullmatch(r'[1-9][0-9]*', string):
        return True
