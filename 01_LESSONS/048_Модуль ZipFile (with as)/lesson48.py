# coding=utf-8
###################################################
# 048_Модуль ZipFile (lesson32 - ДЕРЕВО КАТАЛОГА)
# python 3.x
# WebForMySelf - Андрей Кудлай, 2019
###################################################
# Writing sgiman, 2025

import zipfile
import os

nc = 80
print()

folder_path = './folder'    # архивируемый каталог
zip_file = './test.zip'     # архивный файл
zip_name = 'test.zip'       # name zip file

my_zip = zipfile.ZipFile(zip_file, 'w') # открыть zip-файл на запись (mode: 'w', 'r', 'a')
# my_zip.write('c:\\Python\\folder\\1.txt', compress_type=zipfile.ZIP_DEFLATED, arcname = '1.txt') # variant 1 (запись)
# my_zip.write('c:\\Python\\folder\\1.txt', 'new.txt', compress_type=zipfile.ZIP_DEFLATED) # variant 2 (запись)

for folder, subfolders, files in os.walk(folder_path):  # сканировать иерархию папок (os.walk)
    print(folder, subfolders, files)    # test folders

    for file in files:
        if file == zip_name:    # пропустить, если архив существует
            continue
        # записать zip-архив по полному пути (с "костылями" путей)
        my_zip.write(os.path.join(folder, file),
        os.path.relpath(os.path.join(folder, file), folder_path),
        compress_type=zipfile.ZIP_DEFLATED)

my_zip.close()


########################################################################
# ChatGPT (best code):
# Создать на python c помощью модуля ZipFile упаковщик
# корневого каталога с вложенными каталогами и файлами.
#
########################################################################
import os
import zipfile

#-----------------------------------------------------
# zip_directory()
#-----------------------------------------------------
def zip_directory(folder_path, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)    # полный путь
                # Сохраняем структуру каталогов относительно корня
                arcname = os.path.relpath(file_path, start=folder_path)
                zipf.write(file_path, arcname)

#=========================
# START
#=========================
if __name__ == "__main__":

    root_dir = "./folder"       # Замените на ваш путь
    output_file = "test2.zip"   # Имя создаваемого архива

    zip_directory(root_dir, output_file)

    print('-' * nc)
    print(f"chatGPT: Каталог '{root_dir}' упакован в архив '{output_file}'")

# -----------------------------------------------------------------------
#  - os.walk() рекурсивно обходит все подкаталоги и файлы.
#
#  - arcname используется для сохранения относительного пути
#    внутри архива (без абсолютных путей)
#
# - zipfile.ZIP_DEFLATED — тип сжатия (по умолчанию сжатие gzip).
#
# -----------------------------------------------------------------------
