from django.template.defaultfilters import date, first
from jinja2 import Environment


def environment(**option):
    # 1.创建Environment实例
    env = Environment(**option)

    env.globals.update({
        'date': date,
        'first': first
    })
    return env
