# Основной файл, который управляет игрой:
from game.game import game
from game.score import SevaResult

def start_game():
    """Эта функция управляет всей игрой"""

    print("1. Просмотреть профиль.")
    print("2. Начать игру.")
    print("3. Выйти.")
    while True:
        user_input = int(input("Выберите 1 – 3: "))
        if user_input == 1:
            score_manager = SevaResult()
            score_manager.get_results()
        elif user_input == 2:
            game()
        elif user_input == 3:
            print("До свидания!")
            break
        else:
            print("Ошибка: выберите 1–3")
            user_input = int(input("Выберите 1–3"))
        

start_game()