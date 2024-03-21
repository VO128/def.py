# This is a sample Python script.
def print_params(a=1, b='строка', c=True):

    return (a, b, c)

print(print_params(1, 'строка', True))

print(print_params())

print(print_params(a=25))

print(print_params(c=[1, 2, 3]))

value_list = [2, 3, 4]

value_dict = {'a': 1, 'b': 'строка', 'c': True}

res = print_params(*value_list, **value_dict)

print(res)
