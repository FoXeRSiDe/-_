import random

def password(n):
    result = ""
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result

n = random.randint(3, 20)
print(f"Число из первой вставки: {n}")
print(f"Пароль: {password(n)}")
