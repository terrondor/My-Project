import string
import random


def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_password_strength(password):
    if len(password) < 10:
        return 'Слишком короткий пароль. Минимальная длинна - 10 символов.'

    if not any(char.islower() for char in password):
        return 'Пароль должен содержать хотя бы одну строчную буквву.'

    if not any(char.isupper() for char in password):
        return 'Пароль содержать хотя бы одну заглавную букву.'

    if not any(char.isdigit() for char in password):
        return 'Пароль должен содержать хотябы одну цифру.'

    else:
        return 'Пароль надежный.'


password_length = int(input('Введите желаемую длинну пароля: '))
generated_password = generate_password(password_length)
strength_check = check_password_strength(generated_password)
print('Ваш сгенерированный пароль: ', generated_password)
print('Оценка сложности пароля: ', strength_check)
