import tkinter as tk
from tkinter import messagebox
import string
import random


def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_password_strength(password):
    if len(password) < 10:
        return 'Слишком короткий пароль.'

    if not any(char.islower() for char in password):
        return 'Пароль должен содержать хотя бы одну строчную буквву.'

    if not any(char.isupper() for char in password):
        return 'Пароль содержать хотя бы одну заглавную букву.'

    if not any(char.isdigit() for char in password):
        return 'Пароль должен содержать хотябы одну цифру.'

    else:
        return 'Пароль надежный.'


def on_generate():
    try:
        length = int(entry_length.get())
        if length < 1:
            raise ValueError('Этот пароль слишком короткий.')
        generated_password = generate_password(length)
        password_var.set(generated_password)
        strength = check_password_strength(generated_password)
        strength_var.set(strength)
    except ValueError as e:
        password_var.set('Ошибка: ' + str(e))
        strength_var.set('')


def show_info():
    messagebox.showinfo('Информация', 'Вас приветствует генератор паролей. Он поможет вам сгенерировать пароль.', )


def show_about():
    about_window = tk.Toplevel(window)
    about_window.title('О программе')
    about_window.geometry('300x150')
    about_window.configure(bg='#4e5aea')
    about_window.iconbitmap('password.ico')

    label_about = tk.Label(about_window, text='О программе: \nПрограмма написана \nTerrond 2024 \nversion: 1.0',
                           bg='#4e5aea', fg='white', font=('Arial', 12), justify='center')
    label_about.pack(expand=True)


window = tk.Tk()
window.title('Генератор паролей', )
window.geometry('500x400')
window.configure(bg='#4e5aea', )
window.resizable(width=False, height=False)

# Иконка
window.iconbitmap('password.ico')

# Переменные для пароля и его силы
password_var = tk.StringVar()
strength_var = tk.StringVar()

# Виджеты
label_title = tk.Label(window, text='Генератор паролей', bg='#4e5aea', fg='white', font=('Arial', 14, 'bold'))
label_title.pack(pady=10)

label_length = tk.Label(window, text='Введите желаемую длину пароля:', bg='#4e5aea', fg='white')
label_length.pack(pady=10)

entry_length = tk.Entry(window)
entry_length.pack(pady=10)

button_generate = tk.Button(window, text='Сгенерировать пароль', command=on_generate, bg='#959cf2', fg='white')
button_generate.pack(pady=10)

label_password = tk.Label(window, text='Сгенерированный пароль:', bg='#4e5aea', fg='white')
label_password.pack(pady=10)

label_generated_password = tk.Label(window, textvariable=password_var, bg='#4e5aea', fg='white',
                                    font=('Arial', 12, 'bold'))
label_generated_password.pack(pady=10)

label_strength = tk.Label(window, text='Сила пароля:', bg='#4e5aea', foreground='white')
label_strength.pack(pady=10)

label_strength_message = tk.Label(window, textvariable=strength_var, bg='#4e5aea', foreground='white',
                                  font=('Arial', 12, 'italic'))
label_strength_message.pack(pady=10)

menu = tk.Menu(window)
window.config(menu=menu)

help_menu = tk.Menu(menu)
menu.add_cascade(label='Справка', background='#4e5aea', foreground='white', menu=help_menu, )
help_menu.add_command(label='Информация', background='#4e5aea', foreground='white', command=show_info, )
help_menu.add_command(label='О программе', background='#4e5aea', foreground='white', command=show_about)

# Главный цикл
window.mainloop()
