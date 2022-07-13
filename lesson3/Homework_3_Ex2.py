import time


call_count = 6
start_sleep_time = 0.01
factor = 3
border_sleep_time = 2


def decorator_receiver(call_count_arg, start_sleep_time_arg, factor_arg, border_sleep_time_arg):

    def decorator_repeater(func):

        def wrapper_repeater():
            """Повторение основной функции с вычисляемым интервалом."""
            t = start_sleep_time_arg
            print('Начало работы')
            for i in range(call_count_arg):
                launch_num = i + 1
                result = func()
                print('Запуск номер {}. Ожидание: {} секунд. Результат функции = {}'.format(launch_num, t, result))
                if t <= border_sleep_time_arg:
                    t = start_sleep_time_arg * (factor_arg ** launch_num)
                    if t > border_sleep_time_arg:
                        t = border_sleep_time_arg
                else:
                    t = border_sleep_time_arg
                time.sleep(t)
            print('Конец работы')
            return wrapper_repeater

        return wrapper_repeater

    return decorator_repeater


@decorator_receiver(call_count, start_sleep_time, factor, border_sleep_time)
def repeatable_func():
    """Основная функция."""
    return 'Hello world!'


if __name__ == '__main__':
    repeatable_func()
