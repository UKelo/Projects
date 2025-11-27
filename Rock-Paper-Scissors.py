import customtkinter as ctk
import random as r

# установка тем
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
# создание программы и геометрии
app = ctk.CTk()
app.geometry("550x300")

app.title("Rock-Paper-Scissors")  # заголовок

game = ["rock", "paper", "scissors"]  # список фигур

choice = None
user_select_value = None


def make_user_choice():  # функция вывода выбора пользователя
    choice = r.randint(0, 2)
    global user_select_value
    user_select_value = user_select.get().lower()
    if user_select_value == "rock":
        label.configure(text=f"Твой выбор: {user_select_value} ")
        user_select_value = 0
    elif user_select_value == "paper":
        label.configure(text=f"Твой выбор: {user_select_value} ")
        user_select_value = 1
    elif user_select_value == "scissors":
        label.configure(text=f"Твой выбор: {user_select_value} ")
        user_select_value = 2


def spin():  # функция выводящая победителя
    global choice
    if user_select_value == 0:  # проверка если пользователь выбрал камень
        if choice == 0:
            label.configure(text="Ничья")
        elif choice == 1:
            label.configure(text=f"Компьютер победил, выбор ПК: {game[1]}")
        else:
            label.configure(text="Вы победили!")

    elif user_select_value == 1:  # проверка если пользователь выбрал бумагу
        if choice == 1:
            label.configure(text="Ничья")
        elif choice == 2:
            label.configure(text=f"Компьютер победил, выбор ПК: {game[2]}")
        else:
            label.configure(text="Вы победили!")

    elif user_select_value == 2:  # проверка если пользователь выбрал ножницы
        if choice == 2:
            label.configure(text="Ничья")
        elif choice == 0:
            label.configure(text=f"Компьютер победил, выбор ПК: {game[0]}")
        else:
            label.configure(text="Вы победили!")
    choice = r.randint(0, 2)


btn_choice = ctk.CTkButton(
    master=app, text=("Подтвердите выбор"), command=make_user_choice
)
btn_choice.pack(padx=20, pady=5)

btn_spin = ctk.CTkButton(master=app, text="Кто выйграл?", command=spin)
btn_spin.pack(padx=20, pady=5)

label = ctk.CTkLabel(app, text="", font=("Arial", 16))
label.pack(padx=20, pady=5)

user_select = ctk.CTkComboBox(
    app, values=["rock", "paper", "scissors"], state="readonly"
)
user_select.pack(padx=20, pady=5)

app.mainloop()  # запуск программы
