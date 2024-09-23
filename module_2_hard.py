import random

def password(n):
    result = ""
    for i in range(1, 21):
        for j in range(1, 21):
            if i != j:
                sum = i + j
                if n % sum == 0:
                    result += str(i) + str(j)
    return result

n = 4        #random.randint(3, 20)
print(f"Число из первой вставки: {n}")
print(f"Пароль: {password(n)}")
#Выводит ответ и отзеркаливает
