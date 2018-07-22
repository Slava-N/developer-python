# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import glob
import os.path
import time

migrations = 'Migrations'
files = glob.glob(os.path.join(migrations, '*.sql'))

def search(files, searched_str):
	search_result = []
	for file in files:
		with open(file) as potential_target:
			if searched_str in potential_target.read():
				search_result.append(file)
	return(search_result)

def results(search_result):
	for each_line in search_result:
		print(each_line)
		time.sleep(0.01)
	print('Всего: {}'.format(len(search_result)), sep='\n')


if __name__ == '__main__':
    # ваша логика
    while True:
        searched_str = input('Что Вы хотите найти?\n')
        time.sleep(1)
        search_result = search(files, searched_str)
        results(search_result)
        files = search_result
    pass