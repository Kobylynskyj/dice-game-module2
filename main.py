# Основной файл, который управляет игрой:
from game.game import start_game
from game.score import get_results

def start_game():
    """Эта функция управляет всей игрой"""

    print("1. Просмотреть профиль.")
    print("2. Начать игру.")
    print("3. Выйти.")
    while True:
        user_input = int(input("Выберите 1 – 3: "))
        if user_input == 1:
            get_results()
        elif user_input == 2:
            start_game()
        elif user_input == 3:
            print("До свидания!")
            break
        else:
            print("Ошибка: выберите 1–3")
            user_input = int(input("Выберите 1–3"))
        

start_game()