import os

# Указываем путь к директории
directory = "./sounds"

# Получаем список файлов
files = os.listdir(directory)
files = list(map(lambda x: x[0:-4], files))

# Выводим список файлов
print(files)
