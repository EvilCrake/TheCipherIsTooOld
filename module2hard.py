import random

def generate_password(n):
    result = ""
    for i in range(1, n):
        for j in range(1, 21):
            if i + j == n:
                result += str(i) + str(j)
    return result

# Введите число от 3 до 20
n = random.randint(3, 20)  # Генерация случайного числа от 3 до 20
password = generate_password(n)
print("Случайное число:", n)
print("Пароль для числа", n, ":", password)