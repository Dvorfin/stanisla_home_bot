import os

# Указываем путь к директории
directory = "./sounds"

# Получаем список файлов
files = os.listdir(directory)
files = list(map(lambda x: x[0:-4], files))

# Выводим список файлов
print(files)

with open("users_id.txt", 'r+', encoding="utf-8") as file:
    user_ids = file.readlines()
    for user_id in user_ids:
        print(user_id.strip())