# -*- coding: utf-8 -*-

from importlib import import_module


def get_day(day_tag: str):
    sub_module_name: str = f"day_{day_tag}"
    try:
        day_module = import_module(f"days.{sub_module_name}")
    except:
        return None

    day_class_name = f"Day{day_tag}"
    try:
        day_class = getattr(day_module, day_class_name)
    except:
        return None

    return day_class()
