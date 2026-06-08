# Основной файл, содержащий игровую логику
from game.models import Player, Computer
from game.exceptions import  InvalidRollError
from game.score import save_result
from game.settings import GAME_LEVELS, GAME_LEVELS_CONVERT
import datetime

def get_player_name():
    """Этот блок функций запрашивает имя игрока!"""

    user_name = input("Введите своё имя: ")
    while True:
        if user_name == "":
            print("Ошибка: поле не может быть пустым!")
            user_name = input("Введите своё имя: ")
        elif not user_name[0].isupper():
            print("Имя должно начинаться с большой буквы!")
            user_name = input("Пожалуйста, введите имя ещё раз:  ")
        elif not user_name.isalpha():
            print("Имя может содержать только буквы!")
            user_name = input("Пожалуйста, введите имя ещё раз:  ")
        else:
            print(f"Здравствуйте. 👋 {user_name}")
            break
    return user_name

# Выбор длительности игры.

def get_game_level():
    """Этот блок функций отвечает за выбор длительности игры"""

    long_game = input("Выберите длительность игры 1 - 3: ")
    while True:
        if long_game in GAME_LEVELS:
            raunds = GAME_LEVELS[long_game]
            print(f"{GAME_LEVELS_CONVERT[raunds]} игра ")
            break
        else:
            print("Ошибка!")
            long_game = input("Выберите длительность игры 1 - 3: ")
    return raunds


def start_game():
    """Эта функция запускает игру!"""
    total_score = 0

    name = get_player_name()
    rounds = get_game_level()
    player = Player(name)
    computer = Computer()
    for raund_num in range(1, rounds + 1):
        print(f"\n Раунд {raund_num}")
        while True:
            roll = input("Чтобы начать игру, нажмите Enter: ")
            if roll == "":
                player_roll_dice = player.roll_dice()
                computer_roll_dice = computer.roll_dice()
                print(f"Вы бросили кубик: 🎲 {player_roll_dice}")
                print(f"Компьютер бросил кубик: 🎲 {computer_roll_dice}")
                diff = player_roll_dice - computer_roll_dice
                if diff == 0:
                    print("Ничья. Будет выполнен переброс кубика.")
                    continue
                elif diff > 0:
                    print("Раунд окончен!!!")

                    print(f"Игрок {name} одержал победу.")
                    break
                else:
                    print("Раунд окончен!!!")

                    print("Победил компьютер!")
                    break
            else:
                print(InvalidRollError("Ошибка. Нажмите Enter, чтобы начать игру!"))

        total_score += diff
        print(f"Разница в {diff} очках.")
    print(f"Дата: {datetime.datetime.now().strftime("%Y - %m - %d  %H:%M:%S")}")
    print(f"Игрок: {name}")
    print(f"Количество: {rounds}")
    print(f"Итоговый счет: {total_score}")
    print("---------------------------------")
    save_result(name,rounds,total_score)
    
    

    

