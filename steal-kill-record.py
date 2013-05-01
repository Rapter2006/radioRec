#!/usr/bin/env python
# -*- coding: utf-8 -*-


import subprocess
import os
import datetime
import threading
import shutil


def radioOver():
    print "\nЗавершаем скачку!!!\n"
    subprocess.call(["pkill", "streamripper"])  # остановим стример


def getSounds(time, directory):
    t = threading.Timer(time, radioOver)  # создадим тред, отвечающий за таймер
    t.start()
    subprocess.call(["streamripper", "http://listen.42fm.ru:8000/stealkill-5.0.ogg", directory])  # запустим стример


def pressAll(directory):
    directory2 = directory + "/stealkill-5.0.ogg/"
    files = os.listdir(directory2)  # получим все файлы в директории
    musicOGG = filter(lambda x: x.endswith(".ogg"), files)  # для конвертации возьмем только .ogg файлы
    for i in musicOGG:
        subprocess.call(
            ["ffmpeg", "-i", directory2 + i, "-ab", "120k", directory2 + i[:-3] + "mp3"])  # произведем конвертацию в .mp3
        os.remove(directory2 + i)  # удалим .ogg файл


def renameAndCopy(directory):
    s = datetime.datetime.now().strftime("%d:%m:%y") + "/"  # получим дату
    os.rename(directory + "/stealkill-5.0.ogg/", directory + "/RadioStealKill")  # переименуем папку
    shutil.copytree(directory + "/RadioStealKill/", "/home/rapter/Dropbox/" + s)  # скопируем папку в католог Dropbox'a
    shutil.rmtree(
        directory + "/RadioStealKill/")  # удалим файлы и папку из папки со скриптом, чтобы в дальнейшем не было путаницы


if __name__ == "__main__":
    directory = "/home/rapter/Radio"
    getSounds(3 * 60 * 60, directory)
    pressAll(directory)
    renameAndCopy(directory)
