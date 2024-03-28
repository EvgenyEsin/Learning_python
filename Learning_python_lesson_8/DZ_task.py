# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.


__all__ = ['write_json_csv_pickle']

import os
import json
import csv
import pickle


def write_json_csv_pickle(directory: str):
    # создадим словарь для будущего json файла, csv файла и pickle файла
    result_dict = {}
    for dir_path, file_name in os.walk(directory):
        result_dict[f'DIRECTORY - {dir_path}'] = [f'FILE - {i} = {os.path.getsize(os.path.abspath(dir_path + "/" + i))} byte' for i in file_name]
    # создадим файл json
    with open('json_file_DZ.json', 'w', encoding='utf-8') as json_file: 
        json.dump(result_dict, json_file, indent=4, ensure_ascii=False, separators=(',', ':'))
    # создадим файл csv
    data = [["Dir", "Files"]]
    for key, value in result_dict.items():
        data.append([key, value])
    with open('csv_file_DZ.csv', 'w', encoding='utf-8') as csv_file:
        write_csv = csv.writer(csv_file, dialect='excel-tab', delimiter=',')
        write_csv.writerows(data)
    # создадим файл pickle
    with open('pickle_file_DZ.bin', 'wb') as pickle_file:
        pickle.dump(result_dict, pickle_file)


if __name__ == '__main__':
    write_json_csv_pickle(directory='E:\\Мои уроки\\Data Science в медицине с 4.12.22\\1 год')