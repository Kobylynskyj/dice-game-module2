# Файл для работы с результатами игры:
import json
import datetime

def save_result(player_name, rounds, score):
    try:
        with open("game_result.json", "r", encoding="UTF-8") as json_file:
            game_result = json.load(json_file)
    except:
        game_result = []

    game_result.append({
        "Дата": datetime.datetime.now().strftime("%Y - %m - %d  %H:%M:%S"),
        "Игрок": player_name,
        "Количество раундов": rounds,
        "Итоговый счет": score
    })
    with open("game_result.json", "w", encoding="UTF-8") as json_file:
            json.dump(game_result, json_file, indent=4, ensure_ascii=False)


def get_results():
    with open("game_result.json", "r", encoding="UTF-8") as json_file:
        game_result = json.load(json_file)
        for json_users in game_result:
            print(json_users)

