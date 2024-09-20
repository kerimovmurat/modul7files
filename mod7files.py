
import os
import time

'''Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, 
  os.path.getsize и использование модуля time для корректного отображения времени.'''

directory = '.'  # Указываем путь к каталогу, который хотим обойти
for root, dirs, files in os.walk(directory):  # Обход каталога с использованием os.walk
    for file in files:
        filepath = os.path.join(root, file)  # Формирование полного пути к файлу
        filetime = os.path.getmtime(filepath)  # Получение размера файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) # Получение времени последнего изменения файла
        filesize = os.path.getsize(filepath) # Получение размера файла
        parent_dir = os.path.dirname(filepath) # Получение родительской директории файла
        print (
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: '
            f'{formatted_time}, Родительская директория: {parent_dir}')

