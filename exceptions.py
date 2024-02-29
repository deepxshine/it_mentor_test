class InputError(Exception):
    def __str__(self) -> str:
        return 'Ошибка при вводе данных'


class OperationError(Exception):
    def __str__(self) -> str:
        return 'Данная оперция не поддерживается'
