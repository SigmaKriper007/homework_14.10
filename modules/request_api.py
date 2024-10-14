import requests
# Импортируем функцию read_json для чтения данных JSON
from .read_json import read_json
# Импортируем библиотеку для работы с JSON
import json
# Считываем данные о API ключе и имени города
data_api = read_json(name_file= 'config_api.json')
# Импортируем Api key
API_KEY = data_api['80d7bdb6ff2f2b743df0890c1f9d78c6']
# Утверждаем имя города
CITY_NAME = data_api['city_name']
# Формируем запрос
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
# Выполняем запрос по указанному URL
response = requests.get(URL)
# Проверяем, что запрос выполнен успешно
if response.status_code == 200:
    # Преобразуем полученный ответ в словарь
    data_dict = json.loads(response.content)
    # Выводим полученый ответ с отступами
    print(json.dumps(data_dict, indent= 4))