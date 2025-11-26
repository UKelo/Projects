import customtkinter as ctk
import random as r

# установка темы
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# создание окна
app = ctk.CTk()
app.geometry("550x300")
app.title("> or < or ==")

# количество попыток
attempts = 0

# генерация неизвестного числа
digit = r.randint(1, 100)


# функция рестарта
def restart():
    digit = r.randint(1, 100)
    global attempts
    attempts = 0


# функция ввода числа
def number():
    return int(entry.get())


# функция проверки неизвестного числа и числа введёного пользователем
def test():
    num = number()
    if not (1 <= num <= 100):
        label.configure(text="Введите число от 1 до 100!!!")
    else:
        global attempts
        attempts += 1
        if num == digit:
            label.configure(text="Ты угадал!")
        elif num > digit:
            label.configure(text="Число меньше")
        elif num < digit:
            label.configure(text="Число больше")


# функция возвращающая кол-во попыток
def show_attempts():
    label.configure(text=f"Количество попыток: {attempts}")


# ячейка для ввода
entry = ctk.CTkEntry(app, placeholder_text="Введите число:")
entry.pack(padx=20, pady=(80, 20))

# кнопка проверки
btn_check = ctk.CTkButton(master=app, text="Проверить", command=test)
btn_check.pack(padx=10, pady=5)

# кнопка попыток
btn_attempts = ctk.CTkButton(master=app, text="Попытки", command=show_attempts)
btn_attempts.pack(padx=10, pady=5)

# кнопка перезапуска
btn_restart = ctk.CTkButton(master=app, text="Начать заново", command=restart)
btn_restart.pack(padx=10, pady=5)

# вывод данных в программе
label = ctk.CTkLabel(app, text="", font=("Arial", 16))
label.pack(padx=20, pady=10)

# запуск программы
app.mainloop()
