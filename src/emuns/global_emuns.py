from enum import Enum


class GlobalErrorMessage(Enum):
    WRONG_STATUS_CODE = 'Не то, что мы ожидаем'
    WRONG_LENGTH_COUNT = 'Длина строки не соответствует'
