# ДЗ 1.
# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


__all__ = ['group_rename_files']

import os

def group_rename_files(desired_name, num_digits, original_ext, new_ext, name_range=None):
    file_list = os.listdir('.')
    file_list = [f for f in file_list if f.endswith(original_ext)]

    counter = 1
    for file_name in file_list:
        if name_range:
            original_name_part = file_name[name_range[0]-1:name_range[1]]
        else:
            original_name_part = ''

        new_file_name = '{}_{:0{}}.{}'.format(desired_name + original_name_part, counter, num_digits, new_ext)
        os.rename(file_name, new_file_name)
        counter += 1


if __name__ == '__main__':
    group_rename_files('new_file', 3, '.txt', 'new_txt', [3, 6])
