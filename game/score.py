# Файл для работы с результатами игры:
import json
import datetime

class SevaResult:
        def __init__(self, filename="game_result.json"):
            self.filename = filename
            
        """Эта функция читает"""
        def load_results(self):
            try:
                with open("game_result.json", "r", encoding="UTF-8") as json_file:
                    return json.load(json_file)
            except:
                return []
    
        def save_results(self,player_name, rounds, score):
            game_result = self.load_results()
            game_result.append({
                "Дата": datetime.datetime.now().strftime("%Y - %m - %d  %H:%M:%S"),
                "Игрок": player_name,
                "Количество раундов": rounds,
                "Итоговый счет": score
                })
            with open("game_result.json", "w", encoding="UTF-8") as json_file:
                json.dump(game_result, json_file, indent=4, ensure_ascii=False)

        def get_results(self):
            """Эта функция выводит игроков"""
            for json_users in self.load_results():
                print(f"Дата: {json_users["Дата"]}")
                print(f"Игрок: {json_users["Игрок"]}")
                print(f"Количество раундов: {json_users["Количество раундов"]}")
                print(f"Итоговый счет: {json_users["Итоговый счет"]}")
                print("---------------------------------")



