# def get_multiplied_digits(number):
#     str_number = str(number)
#
#     if len(str_number) > 1:
#         first = int(str_number[0])
#         return first * get_multiplied_digits(int(str_number[1:]))
#     else:
#         return int(str_number)
#
# result = get_multiplied_digits(40203)
# print(result)

def get_multiplied_digits(number):
    str_number = str(number)

    if len(str_number) > 1:
        first = int(str_number[0])
        if first == 0:
            return get_multiplied_digits(int(str_number[1:]))
        else:
            return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number) if str_number != "0" else 1

num = input()
result = get_multiplied_digits(num)
print(result)
