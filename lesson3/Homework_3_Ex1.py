cache = {}


def multiplier_decorator(func):
    """Декоратор функции multiplier."""

    def cache_multiplier(arg: int):
        """Проверяет есть ли результат в кеше. Если есть - выдает число из кеша. Если нет - заносит в кеш."""
        if arg in cache:
            return cache[arg]

        cache.update({arg: func(arg)})
        return func(arg)

    return cache_multiplier


@multiplier_decorator
def multiplier(number: int):
    """Увеличение числа в два раза."""
    return number * 2
