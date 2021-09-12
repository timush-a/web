from django import template

'''
2.1. Фильтр inc. Необходимо в файле extras.py создать фильтр “inc“ который принимает 2 аргумента:
1-й - число которое нужно увеличить, 2-й - на сколько нужно увеличить первое число.
Пример использования фильтра “inc“ представлен в файле template/templates/filters.html

2.2. Тег division. Необходимо в файле extras.py создать тег “division“ (то есть тег для деления),
который принимает 3 параметра: 1-ый - делимое,  2-ой - делитель,  3-ий — флаг определяющий тип возвращаемого
значения для результата деления (именованный аргумент to_int).
Если переданное значение to_int равно False, необходимо выполнить вещественное деление.
Если передано True результат вещественного деления необходимо привести к целому. Значение to_int по-умолчанию — False.

Обратите внимание, что делимое и делитель целые числа, но передаются в тег в формате string.

Пример использования тега “division“ представлен в файле template/templates/filters.html 
'''
register = template.Library()

@register.filter(name='inc')
def inc(number, increase):
    return int(number) + int(increase)

@register.simple_tag
def division(dividend, divider, to_int=False):
    dividend = int(dividend)
    divider = int(divider)

    if not to_int:
        return dividend / divider

    return int(dividend / divider)
