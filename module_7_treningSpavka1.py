# Модуль Ошибки в питоне..
# =======================================
#
# модуль 8_1 Try и Except
# ==========================================
def add_everything_up(a, b):
    isinstance(a, (int, float, str))
    isinstance(b, (int, float, str))
    try:
        return a + b
    except TypeError as exc:
        return f'ошибка сложения типов {a} и {b}, {exc}'
    else:
        return f'нет ошибки {a} + {b}'
    # finally:
    #     return f'программа завершена'

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
