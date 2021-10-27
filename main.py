import time

import requests
import psycopg2
from data import data, chat_id, token
import schedule


def search_python():
    params = {
        'text': 'NAME:Python junior',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'page': 0,  # Индекс страницы поиска на HH
        'per_page': 100,  # Кол-во вакансий на 1 странице
        'period': 1,
        'experience': "noExperience",
    }
    try:
        connection = psycopg2.connect(
            host=data['host'],
            user=data['user'],
            database=data['database'],
            port=data['port'],
            password=data['password'],
        )

        with connection.cursor() as cursor:
            create = """CREATE TABLE IF NOT EXISTS vacancies (
                            id int NOT NULL,
                            name varchar(500) NOT NULL,
                            url varchar(500) NOT NULL
                            );"""
            cursor.execute(create)
            connection.commit()
            print('Table created')

        req = requests.get('https://api.hh.ru/vacancies', params)
        vacancies_list = []
        if len(req.json()['items']) > 2:
            for o in req.json()['items']:
                vacancies_list.append(
                    {
                        'id': o['id'],
                        'name': o['name'],
                        'url': o['alternate_url']
                    }
                )
        db_list = []
        with connection.cursor() as cursor:
            select_command = 'SELECT id FROM vacancies;'
            cursor.execute(select_command)
            db_list.append(cursor.fetchall())
            connection.commit()

        with connection.cursor() as cursor:
            insert_command = 'INSERT INTO vacancies (id, name, url) VALUES (%s, %s, %s);'
            for vac in vacancies_list:
                values = (vac['id'], vac['name'], vac['url'])
                if str(vac['id']) not in str(db_list):
                    cursor.execute(insert_command, values)
                    message = f"{vac['name']}\n{vac['url']}"
                    requests.get(f'https://api.telegram.org/bot{token}/sendMessage',
                                 params=dict(chat_id=chat_id, text=message))
                else:
                    print('Already exists')
            connection.commit()
        # with connection.cursor() as cursor:
        #     cursor.execute('DROP TABLE vacancies;')
        #     print('table pizda')
        #     connection.commit()
    except Exception as ex:
        print(f'[INFO] {ex}')
        pass

    finally:
        if connection:
            print('Connection close')
            connection.close()



def search_django():
    params = {
        'text': 'Django junior',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'page': 0,  # Индекс страницы поиска на HH
        'per_page': 100,  # Кол-во вакансий на 1 странице
        'period': 1,
        'experience': "noExperience",
    }
    try:
        connection = psycopg2.connect(
            host=data['host'],
            user=data['user'],
            database=data['database'],
            port=data['port'],
            password=data['password'],
        )

        with connection.cursor() as cursor:
            create = """CREATE TABLE IF NOT EXISTS vacancies (
                            id int NOT NULL,
                            name varchar(500) NOT NULL,
                            url varchar(500) NOT NULL
                            );"""
            cursor.execute(create)
            connection.commit()
            print('Table created')

        req = requests.get('https://api.hh.ru/vacancies', params)
        vacancies_list = []
        if len(req.json()['items']) > 2:
            for o in req.json()['items']:
                vacancies_list.append(
                    {
                        'id': o['id'],
                        'name': o['name'],
                        'url': o['alternate_url']
                    }
                )
        db_list = []
        print(vacancies_list)
        with connection.cursor() as cursor:
            select_command = 'SELECT id FROM vacancies;'
            cursor.execute(select_command)
            db_list.append(cursor.fetchall())
            connection.commit()

        with connection.cursor() as cursor:
            insert_command = 'INSERT INTO vacancies (id, name, url) VALUES (%s, %s, %s);'
            for vac in vacancies_list:
                values = (vac['id'], vac['name'], vac['url'])
                if str(vac['id']) not in str(db_list):
                    cursor.execute(insert_command, values)
                    message = f"{vac['name']}\n{vac['url']}"
                    requests.get(f'https://api.telegram.org/bot{token}/sendMessage',
                                 params=dict(chat_id=chat_id, text=message))
                else:
                    print('Already exists')
            connection.commit()
    except Exception as ex:
        print(f'[INFO] {ex}')
        pass

    finally:
        if connection:
            print('Connection close')
            connection.close()


schedule.every(10).minutes.do(search_python)
schedule.every(10).minutes.do(search_django)

while True:
    schedule.run_pending()
    time.sleep(1)