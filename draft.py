import time

import requests
import psycopg2
from data import data, chat_id, token
import schedule

try:
    connection = psycopg2.connect(
        host=data['host'],
        user=data['user'],
        database=data['database'],
        port=data['port'],
        password=data['password'],
    )

    # with connection.cursor() as cursor:
    #     cursor.execute('SELECT * FROM vacancies;')
    #     for i in cursor.fetchall():
    #         print(i)
    #     connection.commit()

    with connection.cursor() as cursor:
        cursor.execute('DROP TABLE vacancies;')
        print('table pizda')
        connection.commit()

except Exception as ex:
    print(f'[INFO] {ex}')
    pass

finally:
    if connection:
        print('Connection close')
        connection.close()


# params = {
#     'text': 'Django junior',  # Текст фильтра. В имени должно быть слово "Аналитик"
#     'page': 0,  # Индекс страницы поиска на HH
#     'per_page': 100,  # Кол-во вакансий на 1 странице
#     'period': 1,
#     'experience': "noExperience",
#     'vacancy_label': 'Хуйх'
# }
# req = requests.get('https://api.hh.ru/vacancies', params)
# vacancies_list = []
# if len(req.json()['items']) > 2:
#     for o in req.json()['items']:
#         print(o)