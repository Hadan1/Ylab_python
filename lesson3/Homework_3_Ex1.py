def multiplier_decorator(func):
    """Декоратор функции multiplier."""

    def cache_multiplier(arg: int):
        """Проверяет есть ли результат в кеше. Если есть - выдает число из кеша. Если нет - заносит в кеш."""
        if arg in cache:
            print('Следующий результат будет выведен из кеша')
            return cache[arg]

        cache.update({arg: func(arg)})
        return func(arg)

    return cache_multiplier


@multiplier_decorator
def multiplier(number: int):
    """Увеличение числа в два раза."""
    return number * 2


if __name__ == '__main__':
    cache = {}
    print(multiplier(10))
    print(multiplier(103))
    print(multiplier(1022))
    print(multiplier(1022))
    print(multiplier(100))
    print(multiplier(103))
    print(multiplier(2000))
