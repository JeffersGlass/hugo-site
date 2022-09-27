try:
    x = 1/0
except ZeroDivisionError as err:
    get_console().print_exception(extra_lines=8)