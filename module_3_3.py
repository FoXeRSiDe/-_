def print_params(a=1, b="строка", c=True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [3.14, 'Привет', False]
values_dict = {'a': 42, 'b': 'Мир', 'c': None}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Пока']
print_params(values_list_2, 42)
